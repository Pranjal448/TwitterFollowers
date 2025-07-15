import requests
import json

def load_cookies_from_netscape(file_path):
    cookies = {}
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") and not line.startswith("#HttpOnly_"):
                continue

            if line.startswith("#HttpOnly_"):
                line = line.replace("#HttpOnly_", "", 1)

            parts = line.split("\t")
            if len(parts) == 7:
                name, value = parts[5], parts[6]
                cookies[name] = value
    return cookies

# Enter your user ID here 
# (User ID is different from @username, it only consists of numbers)
user_id = "<enter-user-id>"

cookies = load_cookies_from_netscape("twitter_cookies.txt")

# Enter GraphQL operation ID
url = "https://x.com/i/api/graphql/<enter-GraphQL-operation-ID>/Following"

# Add bearer token here
headers = {
    "authorization": "Bearer <enter-bearer-token>",  
    "x-csrf-token": cookies.get("ct0", ""),
    "x-twitter-active-user": "yes",
    "user-agent": "Mozilla/5.0"
}

features = {
        "responsive_web_edit_tweet_api_enabled": True,
        "responsive_web_enhance_cards_enabled": True,
        "verified_phone_label_enabled": False,
        "creator_subscriptions_tweet_preview_api_enabled": True,
        "tweet_awards_web_tipping_enabled": False,
        "freedom_of_speech_not_reach_fetch_enabled": True,
        "longform_notetweets_consumption_enabled": True,
        "standardized_nudges_misinfo": True,
        "tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled": False,
        "longform_notetweets_rich_text_read_enabled": True,
        "rweb_tipjar_consumption_enabled": True,
        "responsive_web_graphql_timeline_navigation_enabled": True,
        "responsive_web_twitter_article_tweet_consumption_enabled": False,
        "profile_label_improvements_pcf_label_in_post_enabled": True,
        "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
        "communities_web_enable_tweet_community_results_fetch": True,
        "c9s_tweet_anatomy_moderator_badge_enabled": True,
        "articles_preview_enabled": True,
        "rweb_video_screen_enabled": True,
        "payments_enabled": False,
        "view_counts_everywhere_api_enabled": True,
        "responsive_web_grok_analyze_post_followups_enabled": False,
        "responsive_web_grok_analyze_button_fetch_trends_enabled": False,
        "premium_content_api_read_enabled": False,
        "graphql_is_translatable_rweb_tweet_is_translatable_enabled": False,
        "creator_subscriptions_quote_tweet_preview_enabled": False,
        "responsive_web_grok_image_annotation_enabled": False,
        "responsive_web_grok_share_attachment_enabled": False,
        "responsive_web_grok_analysis_button_from_backend": False,
        "responsive_web_grok_show_grok_translated_post": False,
        "longform_notetweets_inline_media_enabled": False,
        "responsive_web_jetfuel_frame": False,
        "responsive_web_grok_community_note_auto_translation_is_enabled": False
} 


all_pages = []
cursor = None

while True:
   
    variables = {
        "userId": user_id,
        "count": 100,
        "cursor": cursor,
    #    "withTweetVisibilityNudge": False,
        "includePromotedContent": False
    }

    params = {
        "variables": json.dumps(variables),
        "features": json.dumps(features)
    }

    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        break

    data = response.json()
    all_pages.append(data)  

    
    cursor = None
    instructions = data.get("data", {}).get("user", {}).get("result", {}).get("timeline", {}).get("timeline", {}).get("instructions", [])
    for instruction in instructions:
        if instruction.get("type") == "TimelineAddEntries":
            for entry in instruction.get("entries", []):
                if entry.get("entryId", "").startswith("cursor-bottom-"):
                    cursor = entry["content"]["value"]
                    break

    if not cursor:
        break  


with open("all_followings_raw.json", "w", encoding="utf-8") as f:
    json.dump(all_pages, f, indent=2, ensure_ascii=False)

print("Saved all pages to all_followings_raw.json")


