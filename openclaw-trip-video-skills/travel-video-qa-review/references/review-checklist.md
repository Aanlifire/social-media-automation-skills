# Review Checklist

## Factual Risk

Flag if the package includes:

- exact current prices
- opening or closing hours
- ticketing and reservation rules
- route closures or transport changes
- visa or entry rules
- weather-sensitive advice
- safety alerts or public incidents
- claims about official policy

Hard current facts need P0 or strong P1 evidence. If evidence is missing, return `needs_fact_check`.

## Script Coherence

Check:

- hook matches the actual topic
- pain point appears in the first few seconds
- scene order is logical
- voiceover and subtitle do not contradict each other
- the travel-planning agent is part of the solution
- CTA is specific and not overloaded

## Advertising Quality

Reject or repair:

- exaggerated savings claims
- guaranteed outcomes
- fake urgency
- repeated hard-sell copy
- unclear product value

Prefer:

- "input city, days, budget"
- "generate a route"
- "avoid detours"
- "compare plan options"

## Media Readiness

Check:

- all scenes have a visual plan
- generated video is not required where static graphics would be clearer
- text fits vertical mobile video
- cover text is short
- brand and subtitles do not fight for the same safe area
- asset prompts avoid copyrighted characters or celebrity likeness

## Platform Risk

Flag:

- automated publishing through fragile cookies
- platform policy-sensitive claims
- impersonation
- reposting or copying creator work
- unlicensed real footage dependence

When unsure, return `human_review_required`.
