import requests

def check_fact_with_google_api(query: str, api_key: str, language='en'):
    url = "https://factchecktools.googleapis.com/v1alpha1/claims:search"
    params = {
        "query": query,
        "languageCode": language,
        "key": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if "claims" not in data:
            return "No fact-check results found."

        results = []
        for claim in data["claims"]:
            text = claim.get("text", "")
            claim_rating = claim.get("claimReview", [{}])[0].get("textualRating", "Not Rated")
            publisher = claim.get("claimReview", [{}])[0].get("publisher", {}).get("name", "Unknown")
            result = f"✔ Claim: {text}\n🗞 Source: {publisher}\n📊 Rating: {claim_rating}"
            results.append(result)

        return "\n\n".join(results)
    except Exception as e:
        return f"❌ Error: {e}"
