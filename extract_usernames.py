import json

with open("all_followings_raw.json", "r", encoding="utf-8") as f:
    all_data = json.load(f)

usernames = []
seen_ids = set()

for page in all_data:
    instructions = (
        page.get("data", {})
            .get("user", {})
            .get("result", {})
            .get("timeline", {})
            .get("timeline", {})
            .get("instructions", [])
    )

    for instruction in instructions:
        if instruction.get("type") != "TimelineAddEntries":
            continue

        entries = instruction.get("entries", [])
        for entry in entries:
            try:
                user = (
                    entry["content"]["itemContent"]["user_results"]["result"]
                )
                user_id = user["rest_id"]
                screen_name = user["core"]["screen_name"]

                if user_id not in seen_ids:
                    seen_ids.add(user_id)
                    usernames.append("@" + screen_name)

            except (KeyError, TypeError):
                continue

# Write to file
with open("followings.txt", "w", encoding="utf-8") as f:
    for username in usernames:
        f.write(username + "\n")

print(f"Extracted {len(usernames)} usernames to followings.txt")
