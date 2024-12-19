from datetime import datetime

def analyze_heartbeat(log_file, key, output_file):
    with open(log_file, "r") as f:
        lines = [line for line in f if key in line]

    lines.sort(key=lambda line: datetime.strptime(line.split("Timestamp ")[1][:8], "%H:%M:%S"))

    previous_timestamp = None
    with open(output_file, "w") as log:
        for line in lines:
            timestamp_str = line.split("Timestamp ")[1][:8]
            current_timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")

            if previous_timestamp:
                time_diff = (current_timestamp - previous_timestamp).total_seconds()

                if time_diff < 0:
                    continue

                if 31 < time_diff < 33:
                    log.write(f"WARNING: {time_diff}s at {timestamp_str}\n")
                    data_found = True
                elif time_diff >= 33:
                    log.write(f"ERROR: {time_diff}s at {timestamp_str}\n")
                    data_found = True

            previous_timestamp = current_timestamp

    if data_found:
        print(f"Analysis complete. Results saved to {output_file}")
    else:
        print(f"No relevant data found to log in {output_file}.")

log_file = "hblog.txt"
key = "TSTFEED0300|7E3E|0400"
output_file = "hb_test.log"

analyze_heartbeat(log_file, key, output_file)