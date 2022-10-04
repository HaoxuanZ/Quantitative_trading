# Quantitative_trading

**Haoxuan Zhang**

**Trading Sectors:**

Risk off sector ETFs represent the companies or products that have relatively low risk. They are the essential things in any period.

Risk on sector ETFs are companies which mostly depend on market effects. These companies are not essential in the hard time, such as financial crisis, and global pandemic

**Optimal Factor Strategies in Volatile Times:**

![](https://github.com/HaoxuanZ/Quantitative_trading/blob/master/riskonoff_cumrets.png)

First, we created two equal weights portfolio allocation for two sectors. Then computed and plot their cumulative performance

In the last part, the risk on sector performance was better than the risk from 1999 to 2020. However, to achieve better performance, we applied our first strategy, which is Equity Volatility Trading. Calculating the actual volatility and comparing magnitude with the VIX index over the past 21 days is required.

After that, it has assigned the entire allocation to risk in a sector that is a bull market. During a bear market, rearrange the allocation to the risk-off sector.

Our portfolio had the best cumulative return of about 393.5%

SPY only had 175.5% at its climax.

![](https://github.com/HaoxuanZ/Quantitative_trading/blob/master/spy_riskonoff.png)

**Introduce GLD to Volatility Trading**

Now, introduce the Gold market into our strategy since the first portfolio did not reach the expected cumulative performance.

Gold is one of the most defensive products for making a hedge. The correlation analysis in the first project should be the best proof.

Gold has a slight correlation of 0 with the S&P500 and VIX. A 0 correlation means two assets have no predictable linear relationship.

We can see more substantial proof of why Gold is so defensive that we can minimize our risk.

During The 2008 Financial Crisis, Gold not only had not been impacted by the crisis but had a solid and incredible performance. Thus, we should use Gold as our insurance in any hard time.

![](https://github.com/HaoxuanZ/Quantitative_trading/blob/master/gld_others.png)

Let us see how well Gold performed in a volatile time strategy.

Our portfolio reached the highest cumulative return, about 588.94%, which is 1.5times more than risk on and risk off the portfolio

For us better seeing the reliability of how Gold can hedge risk to the minimum. Let us see the difference in the Maximum Drawdown between our portfolio and SPY during the COVID Crisis.

Our portfolio MMD is 11.54%, but SPY was down to 31.53% during the COVID Crisis.

![](https://github.com/HaoxuanZ/Quantitative_trading/blob/master/gld_cumrets.png)

![](https://github.com/HaoxuanZ/Quantitative_trading/blob/master/gold_MMD.png)
