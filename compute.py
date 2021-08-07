import sys

__THRESHOLD_MIN_BOUND__ = 0.0
__THRESHOLD_MAX_BOUND__ = 1000000000.0
__LIMIT_MIN_BOUND__ = 0.0
__LIMIT_MAX_BOUND__ = 1000000000.0
__INPUT_MAX_LINES__ = 100


arguments = sys.argv
threshold = 0
limit = 0


if len(arguments) != 3:
    print("python compute.py threshold limit \r\n\tthreshold must be between 0.0 and 1000000000.0 (inclusive)\r\n\tlimit must be between 0.0 and 1000000000.0 (inclusive)")
    exit()

try:
    threshold = float(arguments[1])

except:
    print("Threshold must be a number")
    exit()

try:
    limit = float(arguments[2])
except:
    print("Limit must be a number")
    exit()

errors = []
outputs = []


if (threshold >= __THRESHOLD_MAX_BOUND__) | (threshold < __THRESHOLD_MIN_BOUND__):
    errors.append("Invalid range for threshold. It must be between {0} and {1} (inclusive)".format(
        __THRESHOLD_MIN_BOUND__, __THRESHOLD_MAX_BOUND__))

if (limit >= __LIMIT_MAX_BOUND__) | (limit < __LIMIT_MIN_BOUND__):
    errors.append("Invalid range for threshold. It must be between {0} and {1} (inclusive)".format(
        __LIMIT_MIN_BOUND__, __LIMIT_MAX_BOUND__))


if (len(errors) > 0):
    print("\n".join(_ for _ in errors))
    exit()

output_sum = 0
for line in sys.stdin:
    try:
        input_value = float(line)
        outputs.append(min(limit-output_sum, max(0.0, input_value-threshold)))
        output_sum += min(limit-output_sum, max(0.0, input_value-threshold))
        if len(outputs) >= __INPUT_MAX_LINES__+1:
            errors.append(
                "Input will consist of up to {0} lines of numbers. You have reached this limit.".format(__INPUT_MAX_LINES__))
            break
    except:
        errors.append("Invalid input : {0} is not acceptable".format(
            line.replace("\n", "")))
        break

print("\n".join("{:.1f}".format(_)
      for _ in outputs)+"\n{:.1f}".format(output_sum))
if len(errors) > 0:
    print("\n".join(_ for _ in errors))