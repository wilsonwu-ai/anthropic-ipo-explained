# Anthropic, PBC (proposed Nasdaq: ANT): Initiating-Coverage View at IPO

Prepared 2026-10-27. Not investment advice. No rating and no price target; the scenario values below are arithmetic on stated assumptions, not forecasts.

**Source tags used on every number:** `[S-1]` = the filing (https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm), checked against `anchors/s1.txt`. `[Rep: outlet]` = reported by an outlet, not verified against the filing. `[Mkt: tool, date]` = market data pulled from a tool. `[Asm]` = my assumption. `[Calc]` = my arithmetic on the tagged inputs, formula shown. Where a source conflict exists it is stated. The S-1 leaves price range, share count, raise size and Q3 revenue blank; nothing here fills them from news except where tagged `[Rep]`.

---

## 1. Investment thesis in 3 bullets

1. **Revenue is compounding faster than any comparable at this scale, and the unit economics turned in Q2.** Quarterly revenue went from $376M (Q1 2025) to $11,555M (Q2 2026) `[S-1]`; Q2 2026 operating income was $974M after a $(1,667)M loss in Q1 `[S-1]`; operating cash flow was +$3,929M in H1 2026 vs $(1,513)M in H1 2025 `[S-1]`. Compute and infrastructure fell from 251% of revenue (Q1 2025) to 48% (Q2 2026) `[S-1]`.
2. **The business is mostly pay-per-use by organizations, sold heavily through cloud marketplaces.** Consumption-based revenue was 80% of H1 2026 revenue ($13,064M of $16,286M) `[S-1]`; 48% of H1 2026 revenue came through CSP marketplaces `[S-1]`; customers with $100K+ TTM revenue were more than 11,900 at Sep 30, 2026 `[S-1]` and generated 74% of H1 2026 revenue `[S-1]`. Net Revenue Retention is about 900% `[S-1]`.
3. **The equity is a bet that revenue outruns a fixed compute bill.** Fixed or minimum compute commitments were about $265.6B at Jun 30, 2026 `[S-1]`, with about $245B more signed after that date `[S-1]`, against H1 2026 revenue of $16.3B `[S-1]`. The same S-1 says "revenue is primarily consumption-based, and much of it is not subject to long-term contractual commitments," (S-1, Risk Factors). Long-dated fixed costs against short-dated variable revenue is the whole valuation debate.

---

## 2. Key metrics from the S-1

All dollar figures $M unless noted. `[S-1]` for every input; derived rows are `[Calc]` with the formula shown.

| Metric | FY2023 | FY2024 | FY2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|---|
| Revenue | 41 | 386 | 4,585 | 1,163 | 16,286 |
| Growth (period vs prior comparable) | n/a | +841% | +1,088% | n/a | +1,300% |
| Consumption-based revenue | 39 | 288 | 3,796 | 983 | 13,064 |
| Subscription-based revenue | 2 `[Calc]` = 41 - 39 | 98 | 789 | 180 | 3,222 |
| Consumption share | substantially all | 75% | 83% | n/a | 80% |
| Subscription share | n/a | 25% | 17% | n/a | 20% |
| Cost of revenue | 26 | 752 | 2,773 | 1,019 | 2,380 |
| **Gross margin [Calc] = (Revenue - Cost of revenue) / Revenue** | 36.6% | -94.8% | 39.5% | 12.4% | 85.4% |
| Compute and infrastructure expense | 433 | 2,522 | 7,326 | 2,334 | 8,945 |
| **Compute % revenue [Calc] = Compute / Revenue** | 1,056% | 653% | 160% | 201% | 54.9% |
| Operating income (loss) | (551) | (2,980) | (8,060) | (2,135) | (693) |
| **Operating margin [Calc] = Op. income / Revenue** | n/m | -772% | -175.8% | -183.6% | -4.3% |
| Net loss | (1,531) | (8,309) | (41,965) | (12,969) | (80,748) |
| Operating cash flow | (1,627) | (5,692) | (2,637) | (1,513) | +3,929 |
| Capex (purchases of property and equipment) | (2) | (15) | (131) | n/a | (482) |
| **Op. cash flow less capex [Calc]** | (1,629) | (5,707) | (2,768) | n/a | +3,447 |

Notes on the table:

- **Gross margin is my derivation, not an S-1 line.** The S-1 reports no gross profit. Cost of revenue "consists of compute and infrastructure costs associated with customer-serving workloads" plus some personnel and overhead (S-1, Notes to Consolidated Financial Statements). It excludes compute used for model development, which sits in R&D ($9,741M in H1 2026 `[S-1]`). So 85.4% is a serving-cost margin, not a fully loaded one. The fully loaded view is the compute % revenue row.
- **Net loss is mostly non-cash.** H1 2026 net loss of $(80,748)M includes a $(72,388)M change in fair value of convertible notes, derivatives and SAFEs `[S-1]`. [Calc] 72,388 / 80,748 = 89.6%. Adjusted Operating Income was $1,618M in H1 2026 `[S-1]`; [Calc] 1,618 / 16,286 = 9.9% adjusted operating margin.
- **Quarterly path `[S-1]`:** revenue Q1 25 / Q2 25 / Q3 25 / Q4 25 / Q1 26 / Q2 26 = 376 / 787 / 1,382 / 2,040 / 4,731 / 11,555. Operating income = (935) / (1,200) / (3,089) / (2,836) / (1,667) / 974. Q3 2025 includes a $1.5B Bartz settlement charge `[S-1]`. Q2 2026 operating margin 8% `[S-1]`.
- **Sequential growth `[Calc]`:** Q4 25 = 2,040/1,382 - 1 = +48%; Q1 26 = 4,731/2,040 - 1 = +132%; Q2 26 = 11,555/4,731 - 1 = +144%. Q3 2026 revenue is blank in the S-1. `[Rep: FT via Axios AI+, Oct 2026]` Q3 revenue was $16.8B; [Calc] 16.8/11.555 - 1 = +45%. Sources disagree on the growth label: Reuters (via AI Weekly) says 45%, FT says "nearly 50%". The arithmetic supports 45% against the S-1 Q2 figure.
- **Mix of channels `[S-1]`:** CSP marketplace share of revenue was about 11% (2023), 32% (2024), 47% (2025), 44% (H1 2025), 48% (H1 2026).

### Balance sheet, liquidity and commitments `[S-1]` unless tagged

| Item | Amount | Tag |
|---|---|---|
| Cash and cash equivalents, Jun 30, 2026 | $112,389M | S-1 |
| Short-term investments, Jun 30, 2026 | $19,262M | S-1 |
| Total indebtedness (Amazon convertible notes principal), Jun 30, 2026 | $6.2B | S-1 |
| **Net cash [Calc] = 112,389 + 19,262 - 6,200** | **$125,451M** | Calc |
| Convertible notes payable (carrying value, marked to market) | $108,566M | S-1 |
| Redeemable convertible preferred stock carrying value | $157,510M | S-1 |
| Revolving credit facility (amended Sep 2026) | $15.0B, matures Sep 2031; $5.0B minimum liquidity covenant from Q4 2026 | S-1 |
| Fixed or minimum guaranteed compute commitments, Jun 30, 2026 | about $265.6B, terms 1 to 20 years | S-1 |
| Additional minimum payments from agreements after Jun 30, 2026 | about $245B plus $21B short-term | S-1 |
| Microsoft | at least $44.9B, Nov 2026 to May 2033 | S-1 |
| Google | at least about $114.5B, Apr 2026 to Jul 2033 (plus $125.0B to $150.0B of 2028-2031 TPU compute not in the table) | S-1 |
| Amazon | at least $110.0B, May 2026 to Apr 2036 | S-1 |
| SpaceXAI | up to $120.5B into 2029, about $3.1B per month once delivered | S-1 |
| Nscale / Lambda | up to about $44.6B / about $41.3B | S-1 |
| Broadcom master equipment leases | about $161.2B rent excluding interest (MD&A); Risk Factors cites about $125.2B for the 2026 lease arrangement. The two figures are in the filing as written and I do not reconcile them. | S-1 |
| AMD Helios | no fixed commitment; expected to exceed $20.0B if initial capacity is procured | S-1 |
| Remaining performance obligations | $10.8B | S-1 |
| Commitments vs run-rate [Calc] = 265.6 / 46.22 | 5.7x Q2-annualized revenue | Calc |

Commitment rows are not summed because the filing's tables overlap and some amounts are "up to" or excluded. `[Rep: Opening Bell Daily (Bloomberg), Oct 27]` named compute deals tally to about $637B, about $430B of it minimum or fixed.

---

## 3. Revenue run-rate bases and implied multiples

**Two S-1 bases:**

- H1 2026 x 2 = 16,286 x 2 = **$32,572M** `[Calc on S-1]`. Understates, because H1 includes the slow Q1.
- Q2 2026 x 4 = 11,555 x 4 = **$46,220M** `[Calc on S-1]`. Understates the exit rate if Q3 grew.

**One reported base, kept separate:** Q3 2026 x 4 = 16.8 x 4 = **$67,200M** `[Calc on Rep: FT via Axios AI+]`. Not in the S-1.

**Note on company run-rate:** the S-1 defines Run-Rate Revenue as trailing 28-day consumption fees x 13 plus monthly subscription fees x 12 `[S-1]`. Its value is not used here. `[Rep: Bloomberg via App Economy Insights]` run-rate was $65B at end of June; `[Rep: FT]` investors expect $100B to $120B by year end. Both are rumor-grade for this purpose.

**Valuations are `[Rep]`:** $965B Series H post-money (Axios Pro Rata and Mostly Metrics agree on the figure; they disagree on timing, May vs June close); $1.5T to $2T IPO range (TLDR, Reuters, Daily Upside; the Daily Upside says a cut from $2T to $1.5T is under consideration); $3T from "some investors" at "30x annual revenue" (FT via Morning Brew, Aug 2026). [Calc] $3,000B / 30 = a $100B revenue base implied by that remark. Whether these are pre- or post-money, and before or after IPO proceeds, is not stated in the S-1.

**Implied price-to-sales = Valuation / run-rate revenue** `[Calc]`:

| Valuation `[Rep]` | H1 x 2 ($32.6B) | Q2 x 4 ($46.2B) | Q3 x 4 ($67.2B, Rep) | TTM to Jun 2026 ($19.7B) |
|---|---|---|---|---|
| $965B (Series H) | 29.6x | 20.9x | 14.4x | 49.0x |
| $1.5T | 46.1x | 32.5x | 22.3x | 76.1x |
| $2.0T | 61.4x | 43.3x | 29.8x | 101.5x |
| $3.0T | 92.1x | 64.9x | 44.6x | 152.2x |

TTM revenue [Calc] = FY2025 4,585 - H1 2025 1,163 + H1 2026 16,286 = 19,708 `[S-1]`. TTM lags a hyper-growth company badly and is shown only because the comps below use TTM.

**EV/Sales variant.** [Calc] EV = Valuation - net cash 125.45B (Jun 30, S-1). On Q2 x 4: $1.5T gives (1,500 - 125.45) / 46.22 = 29.7x; $2T gives 40.6x; $3T gives 62.2x. This ignores cash burn since Jun 30 and IPO proceeds `[Rep: $60B to $100B raise]`, so it is a rough guide.

**The reference multiples from the brief, `[Rep: Morning Brew citing FT, Aug 2026]`:** 30x (the $3T remark) and about 55x (Palantir and Nebius). The live comps below show different numbers for those two names; see the table.

---

## 4. Comps

**As of 2026-10-27 (tool timestamp 11:36). Source: `mcp__dubbs-research__equity_price_quote` and `mcp__dubbs-research__equity_fundamental_metrics`, provider yfinance. All values `[Mkt: yfinance via dubbs-research, 2026-10-27]`.** `build_comp_set` was not used. EV/Sales is the tool's `enterprise_to_revenue` (TTM). Revenue growth is the tool's latest-quarter y/y field. yfinance is a free-data provider: treat figures as indicative, not audited. NVDA market cap of $5.25T is consistent with the $5.2T to $5.26T on Oct 26 reported in FACTS (CompaniesMarketCap).

| Ticker | Last price | Market cap ($B) | EV ($B) | EV/Sales (TTM) | Revenue growth | Gross margin | Operating margin |
|---|---|---|---|---|---|---|---|
| NVDA | $217.43 | 5,250.0 | 5,182.0 | 17.1x | +105.9% | 74.7% | 66.2% |
| MSFT | $532.91 | 3,957.1 | 4,006.8 | 12.1x | +17.7% | 67.9% | 45.1% |
| PLTR | $199.36 | 479.1 | 468.7 | 76.1x | +92.8% | 84.8% | 47.1% |
| SNOW | $339.98 | 119.9 | 118.5 | 21.8x | +35.1% | 67.0% | -17.0% |
| CRWV | $58.24 | 32.1 | 76.5 | 10.1x | +112.5% | 67.4% | -1.9% |
| NBIS | $167.80 | 45.6 | 44.2 | 32.6x | +454% | 74.3% | -0.2% |
| ORCL | $129.89 | 393.8 | 518.6 | 7.2x | +29.6% | 64.0% | 35.6% |
| **Median (7)** [Calc] | | | | **17.1x** | | | |
| **Mean (7) / mean ex-PLTR (6)** [Calc] | | | | 25.3x / 16.8x | | | |
| Anthropic, $1.5T on Q2 x 4 [Calc on Rep + S-1] | | 1,500 | | 32.5x (P/S) | +1,368% (Q2 y/y, S-1) | 85.4% (H1, my derivation) | +8% (Q2, S-1) |

Reading the table:

- Anthropic at $1.5T sits at about 1.9x the comp-set median on a Q2 run-rate basis (32.5 / 17.1 [Calc]) and above every comp except PLTR (76.1x) and NBIS (32.6x, level on this basis).
- [Calc] The comp median 17.1x applied to Q2 x 4 gives 17.104 x 46.22 = about $791B; applied to the reported Q3 x 4 base gives 17.104 x 67.2 = about $1,149B. PLTR's 76.1x on Q2 x 4 gives about $3.5T. The comp set brackets $0.8T to $3.5T, which is why the answer depends on which peer Anthropic is said to resemble.
- None of these is a clean peer. MSFT, ORCL and NVDA are profitable at scale; CRWV and NBIS are capacity providers carrying the same hardware risk Anthropic rents. The roughly 55x quoted in August for PLTR and NBIS differs from today's tool values of 76.1x and 32.6x (different date and basis).
- CRWV is the cautionary comp: `[Rep: DealBook (NYT), Oct 15]` more than $35B of debt against a $104B contracted backlog; CRWV's price is $58.24 vs a 52-week high of $141.79 `[Mkt: yfinance, 2026-10-27]`.

---

## 5. Scenarios: 2028 revenue, margin, implied value

**Everything in this section is an `[Asm]` unless it carries another tag.** I built a deliberately simple structure so a reader can change any input:

- Margin = 1 - (Compute / Revenue) - (Other opex % of revenue).
- Compute floor of **$155B in 2028** `[Rep: The Leverage, Oct 26: contracts imply about $120B next year and about $155B by 2028, mostly non-cancelable]`. It is a newsletter derivation from the S-1 commitments, not an S-1 line. I hold it fixed in bear and base because the take-or-pay terms are fixed regardless of demand (S-1, Risk Factors).
- Other opex (personnel, sales and marketing, G&A) for context: in Q2 2026 non-compute operating expenses were (10,581 - 5,558) / 11,555 = 43.5% of revenue `[Calc on S-1]`. Scenario values below are `[Asm]` assuming strong operating leverage.
- Exit value at end of 2028 = 2028 Revenue x EV/Sales multiple `[Asm]`, anchored to the comp range above (ORCL 7.2x, CRWV 10.1x, MSFT 12.1x).
- Discount to today at 12% for 26 months: factor = 1.12^(26/12) = 1.278 `[Asm]`. Net cash and IPO dilution are excluded and assumed to offset (cash is needed to fund the build) `[Asm]`.

| | Bear | Base | Bull |
|---|---|---|---|
| 2028 revenue `[Asm]` | $110B | $260B | $400B |
| Rationale `[Asm]` | Growth stalls near the year-end 2026 run-rate (`[Rep: FT]` $100B to $120B expected) as price wars and open-weight models cap pricing | Q3 run-rate of $67.2B `[Rep]` grows about 3.9x in about 2 years | Agentic demand keeps compounding; OpenAI's own 2030 plan is $350B `[Rep: FT via TNW, Jul 2026]` |
| Compute expense `[Asm]` | $155B (fixed, floor) | $155B | $200B (more capacity bought) |
| Other opex % revenue `[Asm]` | 20% | 15% | 12% |
| **Operating margin [Calc] = 1 - C/R - other%** | 1 - 155/110 - 0.20 = **-60.9%** | 1 - 155/260 - 0.15 = **+25.4%** | 1 - 200/400 - 0.12 = **+38.0%** |
| Operating income [Calc] | -$67B | +$66B | +$152B |
| Exit EV/Sales `[Asm]` | 3x | 8x | 12x |
| Exit value, end 2028 [Calc] = R x multiple | $330B | $2,080B | $4,800B |
| **Implied value today [Calc] = exit / 1.278** | **about $258B** | **about $1,627B** | **about $3,755B** |
| Implied exit EV / operating income [Calc] | n/m (loss) | 31.5x | 31.6x |

Probability-weighted `[Asm]` 25% / 50% / 25%: 0.25 x 258 + 0.50 x 1,627 + 0.25 x 3,755 = **about $1,817B**. The weights are mine, not a forecast.

What the table says, and does not say:

- The base case lands near the low end of the reported $1.5T to $2T range, but that is because I chose the base inputs; it is a consistency check, not evidence.
- The bear case is severe by construction because the compute floor is fixed. In practice the company could re-sell, defer or renegotiate capacity, which would soften it. It is the S-1's own warning made numeric: the S-1 describes minimum-purchase and take-or-pay compute terms that bind Anthropic regardless of utilization (S-1, Risk Factors, my paraphrase) while revenue is largely uncontracted.
- Margin sensitivity is extreme. At the base $260B, each $10B of compute above $155B costs 3.8 points of margin [Calc] 10 / 260.
- The exit multiples carry as much weight as the revenue. 8x to 12x sales for a company at 25% to 38% operating margin implies about 32x operating income, richer than MSFT (20.6x EV/EBITDA) and ORCL (15.1x) on the same tool `[Mkt: yfinance, 2026-10-27]`.

---

## 6. What has to be true for $2T

Target: a value today of $2,000B means an end-2028 exit value of 2,000 x 1.278 = **$2,556B** `[Calc on Asm 12% hurdle]`. The required 2028 revenue is that exit value divided by the exit multiple `[Calc]`; the implied margin uses compute fixed at $155B and other opex at 15% `[Asm]`.

| Exit EV/Sales `[Asm]` | Required 2028 revenue | Multiple of Q3 x 4 ($67.2B, Rep) | Implied operating margin |
|---|---|---|---|
| 8x | $320B | 4.8x | 36.5% |
| 10x | $256B | 3.8x | 24.4% |
| 12x | $213B | 3.2x | 12.2% |

The four conditions:

1. **Revenue roughly 3x to 5x the reported Q3 annualized rate by 2028**, which is the $213B to $320B range above. Q3's sequential growth was 45% `[Calc on Rep]`, down from +144% in Q2 `[S-1]`. Reaching $256B in 2028 `[Asm]` requires growth to stay strong for several more quarters after that deceleration.
2. **Compute cost must not scale with revenue.** At $256B of revenue, $155B of compute is 61% of revenue [Calc] 155/256. That only works if the committed capacity is fully used and monetized; the S-1 flags that agentic offerings "are structurally more compute-intensive" (S-1, Risk Factors).
3. **Pricing holds.** `[Rep: Bloomberg Intelligence via Axios AI+, Oct 15]` Anthropic charges roughly 20% to 30% more than competing models; `[Rep: FT via Morning Brew, Aug]` its top model is 2.5x the price of a comparable OpenAI tool. `[Rep: The Next Web, Sep 22]` OpenAI cut GPT-6 Sol and Luna API prices by 50%. A premium must survive that.
4. **The capital markets stay open.** The company needs to fund the build; `[Rep: Axios AI+, Oct 21]` Anthropic is offering Blackstone above 10% on $9B of junior debt in a $60B chip-financing package, and `[Rep: FT via AI Supremacy]` global AI-related debt issuance fell to $23B in Sep 2026 from $113B in June.

At 12% the $2T case needs the base-or-better scenario; for the $3T "30x revenue" case (`[Rep]` only, not in the S-1) the 2028 requirements scale by about 1.5x [Calc] 3,000 / 2,000.

---

## 7. Five key risks (S-1 citations)

1. **Fixed compute against variable revenue** (S-1, Risk Factors; Management's Discussion and Analysis). About $265.6B fixed or minimum commitments at Jun 30, 2026 plus about $245B more since `[S-1]`; "Compute is the most significant operating cost in our business, and compute efficiency is a critical determinant" (S-1, Management's Discussion and Analysis). Remaining performance obligations were only $10.8B `[S-1]`, so contracted revenue covers a small slice of the bill. Cross-defaults could accelerate the credit agreement and convertible notes (S-1, Risk Factors).
2. **Competition and pricing pressure** (S-1, Risk Factors, competition). The S-1 says rivals may sell "products at zero or negative margins to gain market share, or use their substantial financial resources to" subsidize AI (S-1, Risk Factors), and that "These competitors can outbid us for scarce compute, secure priority" allocations (S-1, Risk Factors). It names OpenAI and Google as primary frontier competitors and warns that open-weight models could force price cuts. `[Rep: Axios AI+, Oct 26 citing The Information]` OpenAI's price undercutting is "producing some results".
3. **Concentration and channel dependence** (S-1, Prospectus Summary; Risk Factors). "A substantial portion of our revenue and accounts receivable is driven by a limited number of" customers and distribution channels (S-1, Prospectus Summary). Top five customers were about 25% of revenue in the nine months to Sep 30, 2026 `[S-1]`; 48% of H1 2026 revenue came through CSP marketplaces `[S-1]`; Amazon, Google and Microsoft are simultaneously suppliers, investors, customers and competitors `[S-1]`. An estimated 5% to 7% of nine-month revenue came from customers later found to violate usage policy or terms `[S-1]`.
3a. *(same bucket, volatility evidence)* `[Rep: App Economy Insights]` customer spend dropped about 20% in the two weeks ended Jan 2 vs the prior two weeks; consumption revenue can move quickly.
4. **Regulatory and political exposure** (S-1, Risk Factors, Legal and Regulatory Matters). A supply-chain-risk designation (Feb 2026); on Sept 25, 2026 the D.C. Circuit ruled 2-1 the designation was proper and Anthropic petitioned for rehearing en banc; in June 2026 the Commerce Department imposed worldwide export restrictions on Fable 5 and Mythos 5, which Anthropic disabled for all customers until lifted `[S-1]`. `[Rep: Morning Brew, Aug 14]` the export controls slowed revenue growth. The S-1 also notes the Department of War suggested it could invoke the Defense Production Act `[S-1]`.
5. **Supply chain and power** (S-1, Risk Factors). "The majority of the world’s most advanced chip manufacturing capacity is concentrated in Taiwan, primarily at" TSMC (S-1, Risk Factors); high-bandwidth memory comes mainly from three suppliers; "The availability of sufficient electrical power has emerged as a" significant constraint (S-1, Risk Factors); some data centers rely on on-site gas generation with fuel costs passed to Anthropic `[S-1]`. `[Rep: Silicon Data via Daily Upside]` token prices have roughly halved since May while GPU rental prices keep rising, a squeeze on the spread.

**Also watch, not in the five:** governance (single Class F share carries 50.1% of votes, Class A capped at 49.9%, Long-Term Benefit Trust elects a board majority `[S-1]`); mark-to-market charges that swing reported net income `[S-1]`; AI safety incidents and FTC demands `[Rep: Axios AI+, Oct 15]`.

---

## 8. Catalysts

| Catalyst | Timing | What the S-1 or reporting says | Tag |
|---|---|---|---|
| Pricing and first trade | Week of Nov 16 targeted; formal marketing as soon as early November; Reuters says debut likely after the November midterms | Price range and share count are blank in the S-1 | Rep: WSJ via DealBook; Bloomberg; Reuters |
| Lock-up expiries | Standard 180 days; co-founders and holders above 0.5% of fully diluted shares are released at the earlier of two days after Q3 2027 results or day 365; other holders at the earlier of two trading days after Q1 2027 results or day 180; Goldman Sachs and Morgan Stanley can release early; some non-founder shares are sellable on the first trading day, others on day 27 and day 48 | Staggered pool sizes are blank in the S-1 | S-1; the 27/48/62 trading-day schedule is Rep: DealBook (NYT), and Yahoo says more than 20 windows over about a year |
| First earnings as a public company | Not stated in the S-1. My expectation is the Q4 2026 print in early 2027 `[Asm]`; Q3 2026 revenue is blank in the filing and the reported $16.8B would be re-checked against it | Watch Q3 operating income, compute % revenue (48% in Q2) and Q3 vs Q4 sequential growth | Asm; S-1 for Q2 baselines |
| Index inclusion | Passive inclusion is uncertain: "In addition, our multi-class capital structure may make us ineligible for inclusion in indices, and as a result," (S-1, Risk Factors). If admitted, fast-entry rules matter. | `[Rep: Yahoo live blog]` SpaceX fell about 15% in its first week in the Nasdaq-100 | S-1; Rep: Yahoo Finance, Oct 26 |
| Legal and policy dates | D.C. Circuit en banc petition outcome; Commerce export restrictions; Nov 3 midterms; FERC large-load interconnection orders | Open items in the S-1 | S-1; Asm for dates not in filing |
| OpenAI cross-read | OpenAI close to a roughly $30B round at about $1.25T (UAE-led); OpenAI IPO expected in 2027 | Revenue comparability: OpenAI books net share via Microsoft, Anthropic books gross via AWS and Google, so the FT's $50B vs Axios $70B gap is accounting basis, not necessarily growth | Rep: CNBC, FT, Axios, Bloomberg |
| Capital-markets read-through | NVDA, CRWV, NBIS and ORCL trade on Anthropic-linked demand; Meta's planned $95B stock sale and Nvidia's $5B-with-peers interest are crowding-in signals | Anthropic compute counterparties include Google, Amazon, Microsoft, SpaceXAI, Broadcom, Nscale, Lambda, AMD | Rep: TLDR, Wall Street Oasis; S-1 for counterparties |

---

## 9. Bottom line

The S-1 supports a company that is now operating-income positive on a quarterly basis and cash-flow positive in H1 2026, growing at an extraordinary rate, and funded with $131.7B of cash plus short-term investments `[Calc: 112,389 + 19,262]`. It also supports a company with about $265.6B of fixed compute obligations, uncontracted consumption revenue, and a political and regulatory risk profile with no direct public-company precedent for its governance. Whether $1.5T to $2T is high depends on three inputs: the multiple a market will pay at scale (8x to 12x sales in my scenarios), whether compute cost stays near $155B in 2028, and whether revenue reaches $213B to $320B. Those are testable with each quarterly print.

*Not investment advice. No rating or price target is given. Market data is from a free provider and may be delayed or wrong; verify before relying on it.*
