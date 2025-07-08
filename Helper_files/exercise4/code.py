# --- Dictionary Logic (inspired by dictex.py) ---
def build_dict_part():
    config = {
        "timeout": 60,
        "retry": 5,
        "mode": "passive",
        "flags": {"debug": True, "verbose": False}
    }

    config.update({"attempts": 3})
    if config.get("flags")["debug"]:
        config["log_level"] = "high"

    priority = config.pop("priority")

    # Use keys and values
    partial = ''.join([str(k)[0] for k in config.keys()])
    return partial + str(priority)


def build_list_part():
    nums = list(range(10, 100, 10))  # [10, 20, ..., 90]

    nums.append(100)
        nums.insert(0, 5)
    nums.remove(30)

    idx = nums.index(999)

    return sum(nums) + str(idx)


def build_tuple_part():
    metrics = (
        (1.0, 0.5),
        (2.5, 1.2),
        (3.1, 4.0)
    )

    # Use zip, tuple comprehension, index access
    scores = tuple(zip([a[0] for a in metrics], [a[1] for a in metrics]))

    
    scores[0][0] = 9.9

    sum_part = sum([int(s[0] + s[1]) for s in scores])  # ❌ also breaks if TypeError doesn't hit first
    return str(sum_part)


# --- Main Function ---
def generate_password():
    d = build_dict_part()
    l = build_list_part()
    t = build_tuple_part()

    return f"{d}-{l}-{t}"


# Will trigger multiple intentional errors
print("Generated Password:", generate_password())
