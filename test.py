import pandas as pd
import matplotlib.pyplot as plt
import json

from main import CECCalculator

QUALITY_THRESHOLD = 128
BATCH_SIZE = 64
SHUFFLE_BUFFER_SIZE = BATCH_SIZE * 2
eeg = pd.read_csv("eeg-data.csv")

unlabeled_eeg = eeg[eeg["label"] == "unlabeled"]
eeg = eeg.loc[eeg["label"] != "unlabeled"]
eeg = eeg.loc[eeg["label"] != "everyone paired"]

eeg.drop(
    [
        "indra_time",
        "Unnamed: 0",
        "browser_latency",
        "reading_time",
        "attention_esense",
        "meditation_esense",
        "updatedAt",
        "createdAt",
    ],
    axis=1,
    inplace=True,
)

eeg.reset_index(drop=True, inplace=True)
eeg.head()

def convert_string_data_to_values(value_string):
    str_list = json.loads(value_string)
    return str_list


eeg["raw_values"] = eeg["raw_values"].apply(convert_string_data_to_values)

eeg = eeg.loc[eeg["signal_quality"] < QUALITY_THRESHOLD]
eeg.head()


def view_eeg_plot(idx):
    data = eeg.loc[idx, "raw_values"]
    # plt.plot(data)
    plt.clf()
    ec = CECCalculator()
    ec.load_data([(i + 1, data[i] + 300) for i in range(len(data))])
    ec.CalcEigenCoordinates()
    ec.CalcEigenCoefficients()
    ec.CalculateParameters()
    ec.CalculatePlotFunctions()
    plt.plot(ec.m_x, ec.m_y)
    a, mu, nu, gamma = ec.CalculateParameters()

    ec_new = CECCalculator()
    ec_new.GenerateData(100, 5, len(data) + 1, a=a, mu=mu, gamma=gamma, nu=nu, rand=0.0)
    ec_new.CalcEigenCoordinates()
    ec_new.CalcEigenCoefficients()
    ec_new.CalculateParameters()

    plt.plot(ec_new.m_x, ec_new.m_y, color='red')

    plt.title(f"α={a:0.4f}, μ={mu:0.4f}, ν={nu:0.4f}, γ={gamma:0.4f} (id={idx})")
    plt.show()


for i in range(0, 10):
    try:
        view_eeg_plot(i)
    except:
        continue
# view_eeg_plot(17)