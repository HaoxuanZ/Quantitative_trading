import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize


def get_data(stock_name,start_date,end_date):
    stock_data = yf.download(stock_name, start=start_date, end=end_date)['Adj Close']
    stock_data.columns = stock_name
    return stock_data

class Test:
    def __init__(self, data,stock_name, risk_free,line=True, sample_num=10000):
        self.stock_name = stock_name
        self.risk_free=risk_free
        self.data = data
        # self.length = len(self.data.columns)
        self.length = len(stock_name)
        self.sample_num = sample_num
        self.simulate(line=line)

    def get_ret_vol_sr(self, weights):
        weights = np.array(weights)
        stock_return = np.sum(self.Log_return.mean() * weights) * 252
        volatility = np.sqrt(
            np.dot(weights.T, np.dot(self.Log_return.cov() * 252, weights))
        )
        sharperatio = (stock_return -self.risk_free)/ volatility
        return np.array([stock_return, volatility, sharperatio])

    def neg_sharpe(self, weights):
        return self.get_ret_vol_sr(weights)[2] * -1

    def check_sum(self, weights):
        # return 0 if sum of the weights is 1
        return np.sum(weights) - 1

    def minimize_volatility(self, weights):
        return self.get_ret_vol_sr(weights)[1]

    def simulate(self, line):
        """
        Optimize our portfolio via Monte-Carlo simulation
        :param line:
        :return:
        """
        self.stock_weights = np.zeros((self.sample_num, len(self.stock_name)))
        self.Return = np.zeros(self.sample_num)
        self.Vol = np.zeros(self.sample_num)
        self.Sharpe_ratio = np.zeros(self.sample_num)
        self.Log_return = np.log(self.data / self.data.shift(1))

        for x in range(self.sample_num):
            self.weights = np.array(np.random.random(self.length))
            self.weights = self.weights / np.sum(self.weights)
            self.stock_weights[x, :] = self.weights
            # calculate portfolio return, vol and sharpe ratio via simulation
            self.Return[x] = np.sum((self.Log_return.mean() * self.weights * 252))
            self.Vol[x] = np.sqrt(
                np.dot(
                    self.weights.T, np.dot(self.Log_return.cov() * 252, self.weights)
                )
            )
            self.Sharpe_ratio[x] = (self.Return[x]-self.risk_free) / self.Vol[x]

        self.front_x = []
        self.front_y = np.linspace(0.20, 0.6, 200)

        for possible_return in self.front_y:
            cons = (
                {"type": "eq", "fun": self.check_sum},
                {
                    "type": "eq",
                    "fun": lambda w: self.get_ret_vol_sr(w)[0] - possible_return,
                },
            )
            init_guess = np.ones(self.length) / (self.length)
            bounds = ((0, 1),) * (self.length)
            self.result = minimize(
                self.minimize_volatility,
                init_guess,
                method="SLSQP",
                bounds=bounds,
                constraints=cons,
            )
            self.front_x.append(self.result["fun"])


    def portfolio_result(self):
        self.optim_number = self.Sharpe_ratio.argmax()
        self.optim_weights = self.stock_weights[self.optim_number]
        print("The Optimal portfolio based on simulation : ")
        for i in range(self.length):
            print(
                "Stock：{}, Weight：{:.2f}%".format(
                    self.data.columns[i], self.optim_weights[i] * 100
                )
            )
        self.best_results_arr = self.get_ret_vol_sr(self.optim_weights)
        print(
            "Expected annualized returns: {:.2f}%, Risk: {:.2f}%, Sharpe Ratio: {:.2f}%".format(
                self.best_results_arr[0] * 100,
                self.best_results_arr[1] * 100,
                self.best_results_arr[2],
            )
        )
        return self.best_results_arr
    def result_array(self):
        self.optim_number = self.Sharpe_ratio.argmax()
        self.optim_weights = self.stock_weights[self.optim_number]
        self.best_results_arr = self.get_ret_vol_sr(self.optim_weights)
        return self.best_results_arr

    def Efficient_frontier(self, line=True):
        plt.figure(figsize=(8, 6))
        plt.scatter(self.Vol, self.Return, c=self.Sharpe_ratio, cmap="plasma", s=10)
        result=self.result_array()
        plt.text(result[1],result[0],'%.2f' % result[2],ha='center', va= 'bottom',fontsize=9)
        plt.plot(result[1],result[0],'r*',markersize=15)
        plt.colorbar(label="Sharpe Ratio")
        plt.xlabel("Volatility")
        plt.ylabel("Return")
        plt.xticks(np.arange(0, 0.8, step=0.05))
        plt.title("Portfolio and Efficient frontier",fontsize=15)
        if line:
            plt.plot(self.front_x, self.front_y, "r--", linewidth=3)
        plt.show()
    def print_portfolio(self):
        self.optim_number = self.Sharpe_ratio.argmax()
        self.optim_weights = self.stock_weights[self.optim_number]
        return self.optim_weights

stock= ["TSLA", "NVDA", "MSFT", "AAPL", "GOOGL", "BRK-B", "AMZN"]
start_date = '2018-01-01'
end_date = '2021-01-01'
All_data=get_data(stock, start_date, end_date)

simu = Test(All_data, stock,risk_free=0.10, sample_num=10000)
simu.portfolio_result()
simu.Efficient_frontier()