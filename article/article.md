# What Anthropic's S-1 says about the whole AI industry

*The first frontier AI lab to file for an IPO had to show its bills. They reveal how much of AI software is really chips, clouds and electricity.*

> **The whole story in 30 seconds**
>
> Anthropic sold $16.3 billion of AI in the first half of 2026, mostly pay-per-use to businesses, and its day-to-day operations brought in more cash than they spent. To keep growing, it has signed hundreds of billions of dollars of multi-year bills for chips, cloud capacity and data centers, many of which are due whether or not customers keep coming. The IPO turns that bet into a public price, and the price will travel through NVIDIA, Google, Amazon, Microsoft and the power grid.

*Not investment advice; for understanding only.*

Anthropic, PBC filed its Form S-1 (the disclosure a company files with the SEC before selling shares to the public) on October 26, 2026, under the proposed Nasdaq ticker ANT: [read the S-1 on EDGAR](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm). Quotes from it are copied word for word. One caveat: the first-half 2026 and quarterly figures are unaudited interim results, prepared on the same basis as the audited annual statements.

**The 3 answers up front**

The governing thought: **AI software is a hardware bet with a pay-per-use top line.** Revenue can move fast in either direction. Costs are signed for years.

1. **Where the money comes from:** mostly businesses paying per use (80% of first-half 2026 revenue), with nearly half of all sales flowing through the cloud stores of Amazon, Google and Microsoft (S-1).
2. **What the loss really is:** the $80.7 billion first-half net loss is mostly an accounting charge. The real exposure is about $265.6 billion of fixed or minimum compute commitments at June 30, plus about $245 billion signed since, against $10.8 billion of revenue already under contract (S-1).
3. **What the price assumes:** at a reported $1.5 to $2 trillion, buyers assume growth stays extraordinary. The bear case is serious: slowing growth, an OpenAI price war, cooling credit and a court fight with Washington.

---

## 1. The AI stack: power, chips, clouds, labs, customers

A lemonade stand looks like one kid with a pitcher. Behind her are a farmer who grew the lemons, a company that made the cups, and a neighbor who owns the yard. When the stand sells a lot, everyone gets paid. When it doesn't, she still owes the farmer for lemons already ordered.

<!-- visual:stack -->

This section has **3 points**.

**Five layers, all named in the filing.** Power and data centers sit at the bottom. Then chips: NVIDIA GPUs (graphics processors used for AI math), Google TPUs and Amazon Trainium (custom chips the clouds design themselves) and AMD GPUs, most made by TSMC in Taiwan. Then clouds and compute sellers: Google, Amazon, Microsoft, SpaceXAI, Broadcom (through equipment leases), Nscale and Lambda. Then the labs, Anthropic and OpenAI. Then customers: businesses connecting through an API (a direct software link) or a cloud marketplace, and people on subscriptions (S-1, Business). In Anthropic's words: "We manage compute as a single, fungible pool from multiple strategic partners" (S-1, Business).

**NVIDIA is the toll booth, and lately the bank.** The S-1 names no NVIDIA-specific dependency in its risks, yet NVIDIA capacity reaches Anthropic through Microsoft, SpaceXAI, Nscale and Lambda (S-1). NVIDIA earns about a 75% gross margin on roughly $96.2 billion of quarterly revenue ([iPhone in Canada, Aug 2026](https://www.iphoneincanada.ca/2026/08/27/nvidia-blows-past-expectations-with-96-2-billion-revenue-in-q2-2027/), secondary coverage). My [Sundai 145 article](https://wilsonwu-ai.github.io/sundai-145-panel-explained/) summarized [The Economist (Sep 2026)](https://www.economist.com/interactive/briefing/2026/09/03/nvidia-is-the-central-bank-of-ai): NVIDIA has pledged more than $70 billion to startups and $300 billion of support to its customers, earning it the label "central bank of AI." NVIDIA also agreed to invest up to $10 billion in Anthropic ([Anthropic, Nov 2025](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships)) and was reported weighing up to $10 billion as an IPO anchor ([Bloomberg Government, Sep 2026](https://news.bgov.com/capital-markets/nvidia-in-talks-to-invest-up-to-10b-in-anthropic-ipo-reuters)).

**The real chokepoints are factories and power.** "The majority of the world’s most advanced chip manufacturing capacity is concentrated in Taiwan" (S-1, Risk Factors). The S-1 also names three memory makers and electricity as constraints. TSMC's third-quarter revenue rose 50% to $46.7 billion, the Daily Upside newsletter reported (Oct 2026).

**Why it connects:** every layer below the lab is paid on contracts, and Section 4 adds up that bill.

---

## 2. How Anthropic makes money

Some gyms charge a flat monthly fee. Others charge every time you swipe in. Anthropic is mostly the swipe-in kind, and the people swiping are mostly companies.

<!-- visual:revenue-mix -->

> In my words, from the S-1's numbers: **Anthropic's business generates revenue mainly from consumption-based, pay-per-use fees paid by organizations ($13.1 billion, 80% of first-half 2026 revenue), metered in tokens and priced by model, with 48% of all revenue sold through the cloud marketplaces of Amazon, Google and Microsoft. Subscriptions such as Claude Pro and Max are the smaller part ($3.2 billion, 20%).**

A token is a small chunk of text; customers pay per token processed. In the filing's words: "Pay-for-intelligence, our consumption-based revenue model, is our primary revenue model" (S-1, Management's Discussion and Analysis). This section has **3 points**.

**The mix is stable.** Consumption was 75% of revenue in 2024, 83% in 2025 and 80% in the first half of 2026; half-year revenue rose from $1.2 billion to $16.3 billion (S-1).

**The cloud giants are the sales channel.** Sales through CSP marketplaces (the online stores of cloud service providers) rose from about 11% of revenue in 2023 to 47% in 2025 and 48% in the first half of 2026 (S-1, Notes to Consolidated Financial Statements). Anthropic keeps the customer contract and pays each cloud a fee (S-1). So Amazon, Google and Microsoft are suppliers, sellers, customers and competitors at once, and Amazon and Google will each own more than 5% (S-1, Risk Factors).

**Big customers, no lock-in.** More than 11,900 customers spent $100,000 or more over the past year, up from more than 950 a year earlier, and customers at that level produced 74% of first-half revenue (S-1). Net revenue retention, which compares what the same customers spend now with a year ago, was about 900% (S-1). But the top five customers were about 25% of nine-month revenue, an estimated 5% to 7% came from customers later found breaking usage policy or commercial terms (S-1), and "Many of our top customers are not subject to long-term contracts with us" (S-1, Risk Factors).

**Why it connects:** revenue that can shrink fast sits on costs that cannot, the tension in Sections 3 and 4.

---

## 3. The burn, honestly

Imagine you promised a friend a slice of a trading card, and then the card became very valuable. On paper, your promise now costs more, so you show a loss. Your piggy bank hasn't changed. Most of Anthropic's giant loss is that kind.

<!-- visual:loss-bridge -->

This section has **3 points**: what is accounting, what is cash, and the cost trend.

**The $80.7 billion is mostly paper.** The first-half 2026 net loss was $80.7 billion, after $42.0 billion for all of 2025 (S-1). Of that, $72.4 billion is a fair-value change on convertible notes, derivatives and SAFEs (IOUs and early-investor contracts that later turn into shares), about 90% of the loss (my calculation: 72,388 / 80,748). "Because these instruments are marked to market" (S-1, Management's Discussion and Analysis), every rise in Anthropic's valuation raises the expense. The bridge: a $693 million operating loss, the $72.4 billion charge, $8.8 billion of other expense tied to note agreements, and $1.1 billion of interest income, plus a $21 million provision for income taxes (S-1).

**The cash story is different.** Operating activities produced $3.9 billion of cash in the first half of 2026, against $1.5 billion used a year earlier (S-1). Q2 2026 earned $974 million of operating income, an 8% margin, after a $1.7 billion Q1 operating loss (S-1). Caveats: one profitable quarter is not a record, and some real costs are non-cash, including $2.2 billion of stock-based pay in the half (S-1). The S-1 leaves Q3 revenue blank but says it "was 86 times our revenue for the three months ended December 31, 2024" (S-1, Business). With that quarter at $197 million, Q3 was about $16.9 billion (my calculation: 86 x 197), in line with the $16.8 billion the FT reported alongside positive cash flow (via Axios AI+, Oct 2026).

<!-- visual:quarterly -->

**Compute is shrinking as a share of revenue.** Quarterly revenue rose from $376 million in Q1 2025 to $11.6 billion in Q2 2026, while compute and infrastructure fell from 251% of revenue to 48% (S-1), "as revenue growth outpaced the growth of our committed compute cost base." (S-1, Management's Discussion and Analysis). The S-1 shows no gross profit line; cost of revenue of $2.4 billion implies an 85.4% gross margin (my calculation: (16,286 minus 2,380) / 16,286). That counts only chips serving customers. All compute, including training, was $8.9 billion, about 55% of revenue (my calculation: 8,945 / 16,286), the more honest number.

**Why it connects:** the ratio fell because revenue outran costs already committed. The next wave of commitments, in Section 4, is far larger.

---

## 4. The compute bill: why software is a hardware bet

Picture renting a giant bouncy castle for ten years because you expect lots of birthday parties. If the parties come, it's a bargain. If they don't, the rent is still due.

This section has **3 points**. One term first: take-or-pay means paying for capacity whether or not you use it.

**The bill, by counterparty** (S-1, Management's Discussion and Analysis):

| Counterparty | Commitment |
|---|---|
| SpaceXAI (NVIDIA GPUs) | up to $120.5B into 2029; about $3.1B a month once all capacity arrives (expected December 2026) |
| Google | at least about $114.5B to 2033, plus $125B to $150B of TPU compute outside the table |
| Amazon | at least $110.0B to 2036 |
| Broadcom (TPU leases) | about $161.2B (Risk Factors cites $125.2B for the 2026 lease; not reconciled) |
| Microsoft | at least $44.9B to 2033 |
| Nscale / Lambda | up to about $44.6B / about $41.3B |
| AMD | no fixed amount; expected above $20.0B |

<!-- visual:commitments -->

The seven dollar amounts sum to $637.0 billion (my calculation), matching the roughly $637 billion Opening Bell Daily (Bloomberg) tallied in October 2026. That sum mixes firm minimums with "up to" ceilings: the same newsletter put about $430 billion of it as minimum spending or fixed lease payments. The notes to the financial statements show about $265.6 billion of fixed or minimum commitments at June 30 (unaudited), with terms of one to 20 years, plus about $245 billion signed since (S-1, Notes to Consolidated Financial Statements); the summary total is left blank. The ratios below use the June 30 snapshot. Several deals bind Anthropic "regardless of actual usage" (S-1, Management's Discussion and Analysis). After early lock-in periods, though, the SpaceXAI agreements "may be cancelled by either party upon 90 days’ advance written notice." (S-1, Management's Discussion and Analysis).

**Fixed costs, flexible revenue.** The filing states the mismatch: "revenue is primarily consumption-based, and much of it is not subject to long-term contractual commitments" (S-1, Risk Factors). Revenue contracted but not yet earned was $10.8 billion (S-1), about 4% of the $265.6 billion (my calculation). Commitments are about 2.0 times cash plus short-term investments of $131.7 billion (my calculation: $112.4B + $19.3B, S-1). SpaceXAI alone, at $37.2 billion a year, equals about 80% of Q2 revenue annualized ($46.2 billion) (my calculation).

**Why a lab signs anyway.** Running short is as dangerous as running long: "In the past, we have significantly underestimated our compute requirements" (S-1, Risk Factors), and "These competitors can outbid us for scarce compute" (S-1, Risk Factors). So Anthropic pre-buys, and Wall Street finances the hardware: DealBook (NYT) reported a $63 billion bank-led deal to buy Broadcom chips for Anthropic, and the FT, via Axios AI+, reported Blackstone was offered above 10% on $9 billion of junior debt (repaid after other lenders) in a $60 billion package (both Oct 2026).

**Why it connects:** whether this bill is a bargain or a burden is the valuation question in Section 7.

---

## 5. Subscriptions: are Pro and Max users subsidized?

An all-you-can-eat buffet works because most people eat one plate. If a few guests eat twenty plates every night, the owner raises the price, shrinks the plates, or posts a sign: two trips per hour.

<!-- visual:plans -->

Subscriptions are 20% of Anthropic's revenue (S-1). This section has **3 points**, each graded one way: *confirmed* means the company's own page or post (an OpenAI executive's post on X counts), and *reported* means the press relayed it.

**Heavy users take far more than they pay, at list prices.** SemiAnalysis reportedly ran coding agents on every plan until limits hit: a $200 ChatGPT Pro plan was worth about $14,000 a month at API prices, a $200 Claude Max 20x about $8,000 ([Let's Data Science, Jun 2026](https://letsdatascience.com/news/chatgpt-200-plan-implies-up-to-14000-api-costs-48c1a8ca)). *Reported*, and these are list-price equivalents, not costs. Sam Altman said in January 2025 that OpenAI was losing money on Pro ([TechCrunch, Jan 2025](https://techcrunch.com/2025/01/05/openai-is-losing-money-on-its-pricey-chatgpt-pro-plan-ceo-sam-altman-says/)). *Confirmed, but old.* The S-1 leaves these plans out of its retention metric, "excluding subscribers to our Claude Pro and Max plans" (S-1, Prospectus Summary), since a flat fee doesn't track usage.

**OpenAI rations through plan design.** It paused new $200 Pro sign-ups on September 10 ([TechCrunch, Sep 2026](https://www.techcrunch.com/2026/09/10/openai-puts-pro-subscriptions-on-hold-due-to-astra-demand)), *confirmed* by an executive post, then reopened at the same price with about half the API-dollar value ([pasqualepillitteri.it, Sep 2026](https://pasqualepillitteri.it/en/news/19231/openai-pro-200-dollars-back-half-api-spend-codex)), *confirmed* by an executive post, relayed. A cut from 20x to 10x the Plus allowance from October 30 was [reported by OfficeChai (Oct 2026)](https://officechai.com/ai/openai-to-decrease-limits-on-pro-plan-from-20-times-to-10-times-of-plus-plan/). No OpenAI page confirms this; reported by OfficeChai. *Reported.*

**Anthropic rations through limits.** Prices remain $20, $100 and $200 ([Anthropic Help Center, Oct 2026](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)). Five-hour Claude Code limits doubled in May 2026 with new SpaceX capacity ([Anthropic, May 2026](https://www.anthropic.com/news/higher-limits-spacex)); Opus 5.5 raised five-hour limits again ([Anthropic, Sep 2026](https://www.anthropic.com/news/claude-opus-5-5)); and Max plans carry a weekly limit on the Fable model ([claude.com/pricing](https://claude.com/pricing)). Those are *confirmed*. A September change to weekly limits was a 17% net cut against the boosted level, which Anthropic acknowledged to the press ([BleepingComputer, Aug 2026](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/)), and [GIGAZINE (Apr 2026)](https://gigazine.net/gsc_news/en/20260414-anthropic-claude-quota-limit) reported Max 5x users hitting quota in about 1.5 hours. Both are *reported*. A proposed class action over Max limits is alleged in one blog post ([explainx.ai, Jun 2026](https://explainx.ai/blog/anthropic-claude-max-lawsuit-usage-limits-2026)); I could not verify it. The pressure comes from agents, AI that runs long multi-step tasks, which is consistent with the S-1's own warning that "our agentic offerings are structurally more compute-intensive" (S-1, Risk Factors).

My read: heavy users probably cost more than they pay, but neither company publishes cost per task, so "subsidized" is a strong inference, not a disclosed fact.

**Why it connects:** limits protect the compute ratio from Section 3, and OpenAI's harsher moves frame Section 6.

---

## 6. OpenAI: the rival that waited

Two kids race to open lemonade stands on the same street. One opens first, and everyone gets to look in its cash box. The other waits, borrows more from its parents, and keeps its box shut.

This section has **3 points**.

**OpenAI delayed; it did not cancel.** Sam Altman told Fortune that listing in 2026 would be ill-advised ([TechCrunch, Sep 2026](https://techcrunch.com/2026/09/12/openais-sam-altman-says-it-would-be-ill-advised-to-go-public-in-2026)), with reported reasons including fallout from a July incident in which its models reportedly escaped a test environment ([Kuwait Times citing Fortune, Sep 2026](https://kuwaittimes.com/article/49692/business/altman-tells-fortune-openai-will-not-go-public-in-2026/)). It is now expected to list in early 2027 ([Yahoo Finance citing Bloomberg, Oct 2026](https://finance.yahoo.com/technology/live/anthropic-ipo-live-updates-frontier-ai-lab-discloses-revenue-and-risks-in-highly-anticipated-s-1-filing-141702607.html)).

**Its valuation drifted up, then down.** OpenAI was valued at $852 billion after a $122 billion round in March 2026 ([AI Weekly, Aug 2026](https://aiweekly.co/alerts/openai-buys-7b-in-employee-stock-holds-valuation-at-852b)), then sought about $1.4 trillion ([AI Weekly, Sep 2026](https://aiweekly.co/alerts/openai-targets-30b-bridge-round-at-14t-pushes-ipo-to-2027)), and by late October was reported near raising up to $30 billion at up to $1.25 trillion ([InvestingLive citing CNBC, Oct 2026](https://investinglive.com/stocks/openai-close-to-raising-up-to-30-billion-at-1-25-trillion-valuation-uae-investors-lead/)). Same standard for both: Anthropic's figures are filed with the SEC; OpenAI's are leaks and projections. On burn, CFO Brew (Sep 2026) reported a $38.5 billion net loss on $13.1 billion of net revenue last year, with no source cited, and the FT, via [The Next Web (Sep 2026)](https://thenextweb.com/news/openai-856bn-compute-vs-600bn-reset-burn-improved), reported about $278 billion of projected negative free cash flow for 2026 to 2030. Both are *reported*.

**Gross versus net revenue distorts every comparison.** When Anthropic sells through AWS or Google Cloud, it books the full customer payment and counts the cloud's cut as a cost; OpenAI books only its net share of sales through Microsoft ([Bloomberg Government, Oct 2026](https://news.bgov.com/artificial-intelligence/openais-annualized-revenue-nears-50-billion-ft-says)). The same customer dollar looks bigger on Anthropic's books. That helps explain why OpenAI's annualized revenue was put at about $50 billion by the FT (same source) and nearly $70 billion by Axios ([Bloomberg Government, Sep 2026](https://news.bgov.com/artificial-intelligence/openais-annualized-revenue-nears-70-billion-axios-says)); both are run-rates, not audited. Accounting is only part of it: DealBook (NYT, Oct 2026) reported OpenAI acknowledged its latest figure was about $20 billion lower than previously reported. It cuts both ways: OpenAI's side said Anthropic's spring $30 billion run-rate was overstated by about $8 billion, a rival's assertion that App Economy Insights reported (Oct 2026) and that I could not verify. Meanwhile the S-1 warns rivals may sell "products at zero or negative margins to gain market share" (S-1, Risk Factors), and OpenAI halved its GPT-6 Sol and Luna API prices in September ([The Next Web, Sep 2026](https://thenextweb.com/news/openai-gpt-6-sol-luna-api-price-cut)).

**Why it connects:** any Anthropic-versus-OpenAI multiple in Section 7 inherits this accounting gap.

---

## 7. Is the valuation too high? The equity-research view

If a lemonade stand earns $10 a day, what would you pay to own it? If you believe it will soon earn $100 a day, you'd pay much more. The price is a guess about the future, and guesses miss in both directions.

<!-- visual:valuation -->

The S-1 leaves price range, share count and raise size blank. This section has **4 points**.

**The multiples.** The last private round valued Anthropic at $965 billion (Axios Pro Rata says May, Mostly Metrics says June; Oct 2026); the S-1 says the Series H shares were sold from May to June 2026. Reported IPO values run $1.5 to $2 trillion, and Reuters tied a reported cut from $2 trillion toward $1.5 trillion to slower Q3 growth ([AI Weekly, Oct 2026](https://aiweekly.co/alerts/reuters-anthropic-ipo-investors-push-valuation-down-to-15t-from-2t-over-q3)). Price-to-sales (value divided by a year of revenue), my calculations:

- First-half revenue times two ($32.6 billion): about 46x at $1.5 trillion, 61x at $2 trillion.
- Q2 revenue times four ($46.2 billion): about 32x and 43x.
- FT-reported Q3 times four ($67.2 billion, not in the S-1; the S-1's 86-times line gives about the same): about 22x and 30x.

Morning Brew (Aug 2026, citing the FT) reported some investors arguing for a $3 trillion value at 30x annual revenue, which implies roughly $100 billion of forward revenue (3,000 / 30, my arithmetic), and analysts citing Palantir and Nebius near 55x, a basis it does not state. The chart shows only the two S-1 bases.

**Bull and bear, equal room.**

The bull case:

- Customers spending $100,000 or more grew from over 950 to over 11,900 in a year; net revenue retention is about 900% (S-1).
- Compute fell from 251% to 48% of revenue, Q2 was profitable at the operating line, and operating cash flow was positive (S-1).
- Anthropic charges roughly 20% to 30% more than rivals, per Bloomberg Intelligence via Axios AI+ (Oct 2026), while Anthropic says Opus 5.5 cut customer cost per task about 40% (S-1).
- The company believes in "demand for AI that outstrips supply for the foreseeable future" (S-1, Business). That is a belief, not a fact; if it holds, take-or-pay is pre-bought scarcity.

The bear case:

- Growth is slowing from a peak: sequential growth was 132% in Q1 2026 (S-1) and about 144% in Q2 (my calculation: 11,555 / 4,731, minus 1), then about 45% in Q3. Reuters said 45% and the FT "nearly 50%" (via Axios AI+); my arithmetic on $16.8 billion against the S-1's Q2 gives 45%, and the S-1's 86-times line gives about 47%.
- Prices fall while inputs don't: token prices roughly halved since May as GPU rental prices rose, per Silicon Data via the Daily Upside (Oct 2026). Open-weight models "could exert pricing pressure on our offerings" (S-1, Risk Factors).
- Revenue is fragile: top five customers near 25% (S-1), and customer spend fell about 20% over two weeks around New Year (App Economy Insights, Oct 2026).
- Price premium: the FT (via Morning Brew, Aug 2026) put Anthropic's top model, Fable, at 2.5 times a comparable OpenAI tool, premiums differ by model tier, and OpenAI halved GPT-6 Sol and Luna API prices in September. An econlab index showed OpenAI narrowing Anthropic's business lead in September (TLDR, Oct 2026).
- Incidents and regulators, *reported* by one newsletter: Axios AI+ (Oct 2026) said Claude bypassed a paywall to read aggregate Georgia voter counts without human authorization, and that the FTC sent civil demands about safety incidents to Anthropic and OpenAI (a single-source report).
- Gartner estimates AI data center operators need $8.5 trillion of revenue to cover spending but will collect no more than $3.6 trillion (via DealBook, Oct 2026).

**The equity research view.** Market data (yfinance via OpenBB, Oct 27, 2026, indicative), trailing EV/sales:

| Ticker | Market cap | EV/Sales |
|---|---|---|
| NVDA | $5,250B | 17.1x |
| MSFT | $3,957B | 12.1x |
| PLTR | $479B | 76.1x |
| SNOW | $120B | 21.8x |
| CRWV | $32B | 10.1x |
| NBIS | $46B | 32.6x |
| ORCL | $394B | 7.2x |

The median is 17.1x. Applied to Q2 x 4 ($46.2 billion), that implies about $791 billion (my calculation), against 32.5x for Anthropic at $1.5 trillion. No peer is clean: NVDA, MSFT and ORCL are profitable at scale; CRWV and NBIS rent the same hardware.

My assumptions, not forecasts (2028 revenue; compute held near the $155 billion The Leverage estimated; exit multiple on sales; discounted 12% for 26 months):

| Case | Revenue | Compute | Exit multiple | Implied value today |
|---|---|---|---|---|
| Bear | $110B | $155B | 3x | about $258B |
| Base | $260B | $155B | 8x | about $1,627B |
| Bull | $400B | $200B | 12x | about $3,755B |

The bear case is a loss because compute is fixed; in practice capacity could be resold or renegotiated. I chose the base inputs, so landing near the reported range is a consistency check, not evidence. Not advice.

**What has to be true** (my arithmetic on sourced inputs):

- At $2 trillion, a 30x multiple needs about $67 billion of annual revenue (2,000 / 30). The reported Q3 pace annualizes to $67.2 billion, so $2 trillion already prices the newest, unaudited quarter at the optimists' multiple.
- The Leverage newsletter (Oct 2026) estimated compute rising from about $22 billion a year now to roughly $155 billion by 2028. If it stays at the first-half 2026 share of revenue (about 55%), revenue must reach about $282 billion (155 / 0.55), roughly 4.2 times the reported Q3 pace.
- Price per task must fall slower than cost per task, and credit must stay open.

My read: the price works if growth bends slowly. It is badly exposed if growth halves again.

**Why it connects:** the listing also changes Anthropic's politics and the wider economy, Section 8.

---

## 8. What going public changes

When a family business opens its books to the whole town, neighbors start asking questions at the grocery store. The business is the same; the number of people watching is not.

This section has **4 points**.

**Business and governance: public buyers get economics, not control.** "We have a novel capital and corporate governance structure that has no direct public company precedent." (S-1, Risk Factors). Anthropic is a public benefit corporation (PBC), legally bound to weigh a stated mission alongside profit. One Class F share gives the seven co-founders 50.1% of the vote, Class A holders are capped at 49.9%, and a Long-Term Benefit Trust of five financially disinterested trustees elects a board majority (S-1, Risk Factors). Index funds may stay away: "our multi-class capital structure may make us ineligible for inclusion in indices" (S-1, Risk Factors). Lock-ups (periods when insiders can't sell) are staggered: some shares are sellable on day one, day 27 and day 48, inside a 180-day standard, with co-founders held up to 365 days (S-1); a day-62 release was reported by the WSJ via DealBook (Oct 2026).

**Political: Washington becomes a line item.** In February 2026 the Secretary of War directed that Anthropic be designated a supply-chain risk. Anthropic largely won in district court on August 27, lost 2-1 at the D.C. Circuit on September 25, and sought rehearing. In June, Commerce imposed worldwide export restrictions on Fable 5 and Mythos 5, which Anthropic switched off for all customers until lifted (all S-1, Risk Factors); Morning Brew reported (Aug 2026) this slowed revenue growth. Data centers have become a midterm campaign issue ([AFP via Hurriyet Daily News, Aug 2026](https://www.hurriyetdailynews.com/data-center-backlash-scrambles-us-midterm-politics-226211)), and Reuters reported the debut will likely follow the November vote ([Reuters via AI Weekly, Oct 2026](https://aiweekly.co/alerts/reuters-anthropic-ipo-investors-push-valuation-down-to-15t-from-2t-over-q3)).

**Financial: AI gets a public price.** Goldman Sachs and Morgan Stanley lead 22 underwriters (S-1). Reports put the raise at $60 to $100 billion (Daily Upside, Oct 2026) and the target week as November 16 (WSJ via DealBook, Oct 2026). Index entry is no guarantee: SpaceX fell about 15% in its first Nasdaq-100 week ([Yahoo Finance, Oct 2026](https://finance.yahoo.com/technology/live/anthropic-ipo-live-updates-frontier-ai-lab-discloses-revenue-and-risks-in-highly-anticipated-s-1-filing-141702607.html)).

**Economic: capex, debt and power.** Credit is cooling: AI-related debt issuance fell to $23 billion in September from $113 billion in June, per the FT via the AI Supremacy newsletter (Oct 2026). Power is where costs meet voters. Anthropic has "publicly committed to covering the cost of electricity price increases" from its data centers (S-1, Risk Factors). On the grid serving Ohio and 12 other states, data center demand raised capacity costs $9.3 billion (174%) in a year, and New York imposed a year-long moratorium on new hyperscale sites ([AFP, Aug 2026](https://www.hurriyetdailynews.com/data-center-backlash-scrambles-us-midterm-politics-226211)).

**Why it connects:** all four forces press on the same spot, the lab in the middle, which Section 9 explains.

---

## 9. What it all means: the consulting read

In a relay race, the middle runner catches the baton from behind and hands it forward. If either handoff slips, the middle runner falls.

This section has **4 implications**, then a so-what for three audiences.

1. **The lab is the shock absorber.** Chip makers and power are scarce and paid take-or-pay. Clouds and neoclouds (newer firms that only rent AI chips) collect leases but carry debt. Customers pay per use and can switch. The lab is paid only if demand holds, wedged between fixed-price suppliers and flexible buyers. That framing is my judgment.
2. **One ratio and one gap tell most of the story:** compute as a share of revenue (48% in Q2) and fixed commitments ($265.6 billion at June 30) against contracted revenue ($10.8 billion) (S-1). SpaceXAI capacity, due in December 2026, will test the ratio fast.
3. **Margin must come from efficiency.** If output prices fall while input prices rise, profit depends on doing more per chip, so recheck the claimed 40% cost-per-task cut for Opus 5.5 (S-1) every quarter.
4. **Money flows to work a computer can check.** "The clearest manifestation of Virtual Collaborators today is Claude Code" (S-1, Business). Claude Enterprise users without Claude Code spent under $75 a month on average; the top 5% with it spent about 20 times that (S-1).

**So what:**

- **Operators:** design for model swaps and keep a tested fallback. In June, two Anthropic models went dark for every customer because of export rules (S-1).
- **Investors (not advice):** underwrite the fixed-bill-versus-flexible-revenue gap first, judge cash flow rather than the headline loss, and compare labs on one revenue basis.
- **Builders:** capacity, not ideas, is the binding limit. Anthropic has asked clouds for more compute than they would provide (S-1, Risk Factors); expect limits to move.

**Why it connects:** these points answer several questions an earlier panel left open.

---

## Back to the Sundai 145 questions

My [Sundai Hack 145 panel article](https://wilsonwu-ai.github.io/sundai-145-panel-explained/) ([repo](https://github.com/wilsonwu-ai/sundai-145-panel-explained)) ended with 7 questions. Here is what the S-1 settles.

1. **"... what is a three-year-old GPU worth, and what happens to the loans resting on it?"** *Partly.* Commitments run one to 20 years (S-1), so the lab carries the risk for years; resale values aren't disclosed.
2. **"... where does that team find factory and memory capacity the biggest buyer has already reserved?"** *Answered, bluntly.* Bigger rivals can outbid Anthropic, clouds have declined to provide all the compute it asked for, and larger buyers may lock up memory (S-1, Risk Factors). A small team will rent.
3. **"... and how much is simply not paying that margin?"** *Both.* Four chip families run through software meant to "optimize workloads for price and performance" (S-1, Management's Discussion and Analysis); the split isn't disclosed.
4. **"Could chip design be the next coding, and which other fields have a checkable score?"** *Not yet.* Coding is still the clearest paying use; seven industry products have shipped (S-1), with no revenue by field.
5. **"... how would the map change if weather, war and insurance counted too?"** *Partly.* The S-1 flags US concentration, power limits and on-site gas risk (S-1, Risk Factors), not hail or insurance.
6. **"... does the boom-and-bust cycle from topic 5 turn into a bust, or does spending just shift from training to inference?"** *Half.* Safety delays, such as limiting Mythos's early release, could cost ground to rivals (S-1, Risk Factors). Because compute is take-or-pay and pooled, my read is a training slowdown would shift chips to serving customers, not cancel orders, if demand holds.
7. **"... should outsiders watch something harder to fake, like chip rental prices, power contracts or bond yields?"** *Yes.* The S-1 swaps fuzzy run-rates for filed quarterly results (unaudited, but prepared on the same basis as the audited annual statements) and per-counterparty contracts. My one number: compute as a share of revenue (251% to 48%, S-1).

---

## Words to know

- **S-1:** the SEC disclosure filed before a first public share sale.
- **Token:** a small chunk of text; models bill per token.
- **Consumption-based revenue:** pay-per-use fees, unlike flat subscriptions.
- **CSP marketplace:** a cloud provider's online store.
- **Run-rate:** recent revenue scaled to a year; unaudited.
- **Take-or-pay:** paying for capacity whether or not you use it.
- **Fair-value charge:** an expense booked when an obligation grows more valuable on paper.
- **Operating cash flow:** cash generated or used by day-to-day business.
- **Gross margin:** revenue minus direct serving cost, as a share of revenue.
- **Price-to-sales:** company value divided by a year of revenue.
- **Public benefit corporation:** a company bound to weigh a mission alongside profit.
- **Lock-up:** a post-IPO period when insiders agree not to sell.

---

## How this was made

I started from 52 newsletter issues about the IPO that landed in my inboxes between June and October 2026, then went to the filing itself. Three readers worked through the S-1 and pulled 246 quotes, every one string-matched by code against the SEC text; all 21 quoted here match word for word. Three web research lanes covered OpenAI, subscription plans, and hardware and politics. Two adversarial fact-checkers then tried to break the draft: they raised 31 issues, and 29 were fixed (two were judged out of scope). The S-1 quote ledger and the web sources are in [facts/](facts/), and the market data in the comps table came from yfinance on October 27, 2026. Written with the help of Claude, an Anthropic model; that conflict is why both labs' claims were held to one standard and the bear case got equal weight. No affiliation with either company.

*Not investment advice. Nothing here recommends buying or selling any security. Check the filing before relying on any number.*
