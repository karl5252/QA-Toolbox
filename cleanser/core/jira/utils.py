import random
import time

from cleanser.const.jira import TIMEOUT, MAX_RETRIES, MIN_WAIT, MAX_WAIT


def safe_post(session, url, data=None):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = session.post(url, json=data, timeout=TIMEOUT)
            if response.status_code == 429:
                raise Exception("Rate limited")
            return response
        except Exception as e:
            print(f"[Retry {attempt}/{MAX_RETRIES}] Failed: {e}")
            if attempt < MAX_RETRIES:
                wait = random.uniform(MIN_WAIT, MAX_WAIT)
                print(f"→ Waiting {wait:.1f}s before retrying...")
                time.sleep(wait)
            else:
                print("Max retries reached. Skipping.")
                return None
