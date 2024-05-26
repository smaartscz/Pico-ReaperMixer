import pinout
import modules.tracks as tracks
import modules.colors as colors
import math

class KalmanFilter:
    def __init__(self, process_variance, measurement_variance, estimated_measurement_variance=1):
        self.process_variance = process_variance
        self.measurement_variance = measurement_variance
        self.estimated_measurement_variance = estimated_measurement_variance
        self.posteri_estimate = 0.0
        self.posteri_error_estimate = 1.0

    def update(self, measurement):
        priori_estimate = self.posteri_estimate
        priori_error_estimate = self.posteri_error_estimate + self.process_variance

        blending_factor = priori_error_estimate / (priori_error_estimate + self.measurement_variance)
        self.posteri_estimate = priori_estimate + blending_factor * (measurement - priori_estimate)
        self.posteri_error_estimate = (1 - blending_factor) * priori_error_estimate

        return self.posteri_estimate
    
def read_filtered_adc(adc,alpha=0.1, num_samples=15):
    """
    Read the ADC value and apply a simple moving average filter.\n
    Parameters:\n
    adc: ADC object to read from.\n
    num_samples: Number of samples to average.\n

    Return:\n
    Filtered ADC value.\n
    """
    total = 0
    for _ in range(num_samples):
        total += adc.read_u16()
    average = total / num_samples
    filtered_value = average / 65535.0

    for _ in range(num_samples):
        current_value = adc.read_u16() / 65535.0
        filtered_value = alpha * current_value + (1 - alpha) * filtered_value

    return filtered_value

def linear_to_logarithmic(value):
    """
    Convert a linear potentiometer reading to a logarithmic scale.
    Parameters:\n
    value: Linear value in the range [0, 1].\n
    Return:\n
    Logarithmic value in the range [0, 1].
    """
    if value <= 0.01:
        return 0
    # Apply a logarithmic scale transformation
    min_db = -100.0  # Minimum dB value (adjust as necessary)
    if value <= 0:
        return 0
    # Apply a logarithmic scale transformation
    log_value = min_db * (1 - value)
    return 10 ** (log_value / 20)  # Convert dB to linear scale

async def sliders():
    """
    Check if any slider updated its value.
    Calls:
    tracks.get_mapped_tracks()
    tracks.update_track()
    """
    kalman_filters = [KalmanFilter(1e-3, 1e-2) for _ in pinout.sliders]
    map = await tracks.get_mapped_tracks()

    try:
        for track in map:
            slider_index = int(track["slider"]) - 1

            if slider_index >= len(pinout.sliders):
                print(colors.red + f"Slider index {slider_index} out of range for track {track['name']}" + colors.reset)
                continue

            # Read the filtered slider value from the corresponding pin
            raw_value = pinout.sliders[slider_index].read_u16() / 65535.0
            filtered_value = kalman_filters[slider_index].update(raw_value)
            log_slider_value = linear_to_logarithmic(filtered_value)
            new_slider_value = round(log_slider_value, 5)  # Round to two decimal places
        
            if abs(new_slider_value - track["slider_value"]) > 0.00078:  # Adjust threshold as necessary
                print(colors.blue + f"Slider for {track['name']} changed from {track['slider_value']} to {new_slider_value}" + colors.reset)
                track["slider_previous"] = track["slider_value"]
                track["slider_value"] = new_slider_value
                await tracks.update_track(track['tracknumber'], "slider", new_slider_value)
    except Exception as e:
        print(colors.red + f"Error: {e}" + colors.reset)

async def mute():
    """
    Check if any mute button updated its value.
    Calls:
    tracks.get_mapped_tracks()
    tracks.update_track()
    """
    map = await tracks.get_mapped_tracks()

    try:
        for track in map:
            mute_index = int(track["mute"]) - 1

            if mute_index >= len(pinout.mute):
                print(colors.red + f"mute index {mute_index} out of range for track {track['name']}" + colors.reset)
                continue

            # Read the mute value from the corresponding pin
            current_mute_value = pinout.mute[mute_index].value()
            previous_mute_value = track.get("mute_previous", False)

            # Check for rising edge (transition from not pressed to pressed)
            if current_mute_value and not previous_mute_value:
                # Toggle the mute value
                new_mute_value = not track["mute_value"]

                print(colors.blue + f"Mute for {track['name']} toggled to {new_mute_value}" + colors.reset)
                track["mute_previous"] = current_mute_value
                track["mute_value"] = new_mute_value
                await tracks.update_track(track["tracknumber"], "mute", '-1')
            else:
                # Update the previous state without toggling
                track["mute_previous"] = current_mute_value

    except Exception as e:
        print(colors.red + f"Error: {e}" + colors.reset)
