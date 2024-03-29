{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shird-0/my-projects/blob/main/Titanic\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BQPmz8L9d1aY"
      },
      "outputs": [],
      "source": [
        "import os\n",
        "from google.colab import drive"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "gdrive_dir = '/content/drive/'\n",
        "\n",
        "drive.mount(gdrive_dir, force_remount=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1OueS5c08TpC",
        "outputId": "add1dbd7-a8fd-49bf-dffd-2cea53fbcd59"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive/\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for dirname, _, filenames in os.walk('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data'):\n",
        "    for filename in filenames:\n",
        "        print(os.path.join(dirname, filename))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7ljTQagc8Vn4",
        "outputId": "07e45147-dd59-4ca9-98d7-c81c05e8385f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/gender_submission.csv\n",
            "/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/test.csv\n",
            "/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/train.csv\n",
            "/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/titanic_clean.csv\n",
            "/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/train_features.csv\n",
            "/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/val_features.csv\n",
            "/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/test_features.csv\n",
            "/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/train_labels.csv\n",
            "/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/val_labels.csv\n",
            "/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/test_labels.csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Import libraries\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "\n",
        "from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.metrics import accuracy_score, precision_score, recall_score"
      ],
      "metadata": {
        "id": "GLJM7D799IT4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Import dataset\n",
        "titanic = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/train.csv')"
      ],
      "metadata": {
        "id": "0IZVcwM79Jbv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "titanic.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "yCHb100o-Glm",
        "outputId": "6bbb98e5-6291-4b08-862b-2ee048fe21be"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-28cbccf3-3689-41dc-9b68-c63cf3345e86\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>PassengerId</th>\n",
              "      <th>Survived</th>\n",
              "      <th>Pclass</th>\n",
              "      <th>Name</th>\n",
              "      <th>Sex</th>\n",
              "      <th>Age</th>\n",
              "      <th>SibSp</th>\n",
              "      <th>Parch</th>\n",
              "      <th>Ticket</th>\n",
              "      <th>Fare</th>\n",
              "      <th>Cabin</th>\n",
              "      <th>Embarked</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Braund, Mr. Owen Harris</td>\n",
              "      <td>male</td>\n",
              "      <td>22.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>A/5 21171</td>\n",
              "      <td>7.2500</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
              "      <td>female</td>\n",
              "      <td>38.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>PC 17599</td>\n",
              "      <td>71.2833</td>\n",
              "      <td>C85</td>\n",
              "      <td>C</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>Heikkinen, Miss. Laina</td>\n",
              "      <td>female</td>\n",
              "      <td>26.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>STON/O2. 3101282</td>\n",
              "      <td>7.9250</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
              "      <td>female</td>\n",
              "      <td>35.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>113803</td>\n",
              "      <td>53.1000</td>\n",
              "      <td>C123</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Allen, Mr. William Henry</td>\n",
              "      <td>male</td>\n",
              "      <td>35.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>373450</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-28cbccf3-3689-41dc-9b68-c63cf3345e86')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-28cbccf3-3689-41dc-9b68-c63cf3345e86 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-28cbccf3-3689-41dc-9b68-c63cf3345e86');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "   PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked\n",
              "0            1         0       3  ...   7.2500   NaN         S\n",
              "1            2         1       1  ...  71.2833   C85         C\n",
              "2            3         1       3  ...   7.9250   NaN         S\n",
              "3            4         1       1  ...  53.1000  C123         S\n",
              "4            5         0       3  ...   8.0500   NaN         S\n",
              "\n",
              "[5 rows x 12 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Count missing values\n",
        "titanic.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XfKsIalg-Q0j",
        "outputId": "19762912-235d-47fa-c245-3f703cac5461"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "PassengerId      0\n",
              "Survived         0\n",
              "Pclass           0\n",
              "Name             0\n",
              "Sex              0\n",
              "Age            177\n",
              "SibSp            0\n",
              "Parch            0\n",
              "Ticket           0\n",
              "Fare             0\n",
              "Cabin          687\n",
              "Embarked         2\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Fill missing values\n",
        "titanic['Age'].fillna(titanic['Age'].mean(), inplace=True)"
      ],
      "metadata": {
        "id": "v4esb3A7CJRF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Combine SibSp & Parch\n",
        "for i, col in enumerate(['SibSp', 'Parch']):\n",
        "  plt.figure(i)\n",
        "  sns.catplot(x=col, y='Survived', data=titanic, kind='point', aspect=2)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 738
        },
        "id": "GjY83HBoCwer",
        "outputId": "cdf4cfa9-ce5e-4dd5-92ef-6ea0ee6b72d9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 0 Axes>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 720x360 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAsgAAAFgCAYAAACmDI9oAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nOzdd3zV1eH/8dfJnoSEJKwQZiBhyhBE2aCyFOuquFp3ta0L9adVq3V+bcVZtc5abK3aahURUdlTlshMwggrrCQEQshO7vn9ccPlQiJEzc0n4/18PHiY+7mfe/MWr7nvnHs+5xhrLSIiIiIi4ubndAARERERkfpEBVlERERExIsKsoiIiIiIFxVkEREREREvKsgiIiIiIl4CnA7wY40dO9bOmjXL6RgiIiIi0vCZ6g42uBHknJwcpyOIiIiISCPW4AqyiIiIiIgvqSCLiIiIiHhRQRYRERER8aKCLCIiIiLiRQVZRERERMSLCrKIiIiIiBcVZBERERERLyrIIiIiIiJeVJBFRERERLz4rCAbY94xxmQZYzb8wP3GGPOSMWarMWadMaafr7KIiIiIiNSUL0eQ3wXGnuL+cUBS5Z+bgdd8mEVEREREpEYCfPXE1tqFxpgOpzhlEjDNWmuBb40xzY0xra21+3yVSUSkKbjm7eVkHioiITqU924Y5HQcEZEGx2cFuQbaAru9bmdWHqtSkI0xN+MeZSYxMbFOwomINFSZh4rYnlPgdAwRkQarQVykZ619w1o7wFo7IC4uzuk4IiIiItKIOVmQ9wDtvG4nVB4TEREREXGMkwV5OnBt5WoWZwF5mn8sIiIiIk7z2RxkY8y/gRFArDEmE3gECASw1v4NmAmMB7YChcB1vsoiIiIiIlJTvlzFYvJp7rfAb331/UVEREREfooGcZGeiIiIiEhdUUEWEREREfGigiwiIiIi4kUFWURERETEiwqyiIiIiIgXFWQRERERES8qyCIiIiIiXlSQRURERES8qCCLiIiIiHhRQRYRERER8aKCLCIiIiLiRQVZRERERMSLCrKIiIiIiBcVZBERERERLyrIIiIiIiJeVJBFRERERLyoIIuIiIiIeFFBFhERERHxooIsIiIiIuJFBVlERERExIsKsoiIiIiIFxVkEREREREvKsgiIiIiIl5UkEVEREREvKggi4iIiIh4UUEWEREREfGigiwiIiIi4kUFWURERETEiwqyiIiIiIgXFWQRERERES8qyCIiIiIiXlSQRURERES8qCCLiIiIiHhRQRYRERER8aKCLCIiIiLiRQVZRERERMSLCrKIiIiIiBcVZBERERERLyrIIiIiIiJeVJBFRERERLyoIIuIiIiIeFFBFhERERHxooIsIiIiIuJFBVlERERExIsKsoiIiIiIFxVkEREREREvKsgiIiIiIl58WpCNMWONMenGmK3GmPuruT/RGDPPGLPGGLPOGDPel3lERERERE7HZwXZGOMPvAKMA7oDk40x3U867SHgI2ttX+AK4FVf5RERERERqQlfjiAPBLZaazOstaXAB8Ckk86xQLPKr6OAvT7MIyIiIiJyWr4syG2B3V63MyuPeXsUuNoYkwnMBH5f3RMZY242xqwyxqzKzs72RVYREREREcD5i/QmA+9aaxOA8cB7xpgqmay1b1hrB1hrB8TFxdV5SBERERFpOnxZkPcA7bxuJ1Qe83YD8BGAtXYZEALE+jCTiIiIiMgp+bIgrwSSjDEdjTFBuC/Cm37SObuA0QDGmBTcBVlzKERERETEMT4ryNbacuB3wFdAKu7VKjYaYx4zxlxYedoU4CZjzFrg38CvrbXWV5lERERERE4nwJdPbq2difviO+9jf/T6ehNwji8ziIiIiIj8GE5fpCciIiIiUq+oIIuIiIiIeFFBFhERERHxooIsIiIiIuJFBVlERERExIsKsoiIiIiIFxVkEREREREvKsgiIiIiIl5UkEVEREREvKggi4iIiIh4UUEWEREREfGigiwiIiIi4kUFWURERETEiwqyiIiIiIgXFWQRERERES8qyCIiIiIiXlSQRURERES8qCCLiIiIiHhRQRYRERER8aKCLCIiIiLiRQVZRERERMSLCrKIiIiIiBcVZBERERERLyrIIiIiIiJeVJBFRERERLyoIIuIiIiIeFFBFhERERHxooIsIiIiIuJFBVlERERExIsKsoiIiIiIFxVkEREREREvKsgiIiIiIl5UkEVEREREvKggi4iIiIh4UUEWEREREfGigiwiIiIi4kUFWURERETES4DTAUR87Zq3l5N5qIiE6FDeu2GQ03FERESknlNBlkYv81AR23MKnI4hIiIiDYSmWIiIiIiIeFFBFhERERHxooIsIiIiIuJFBVlE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\n",
            "text/plain": [
              "<Figure size 720x360 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "titanic['Family_count'] = titanic['SibSp'] + titanic['Parch']"
      ],
      "metadata": {
        "id": "msMkGeMcDlRg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "titanic.drop(['PassengerId', 'SibSp', 'Parch'], axis=1, inplace=True)"
      ],
      "metadata": {
        "id": "wF5ctGKoMEdr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "titanic.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "gIVLTCRAMlKl",
        "outputId": "1649a7be-826a-41e0-ebb2-96914b6927c7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-9508c436-35f4-4f62-af4b-36b2f568bce5\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Survived</th>\n",
              "      <th>Pclass</th>\n",
              "      <th>Name</th>\n",
              "      <th>Sex</th>\n",
              "      <th>Age</th>\n",
              "      <th>Ticket</th>\n",
              "      <th>Fare</th>\n",
              "      <th>Cabin</th>\n",
              "      <th>Embarked</th>\n",
              "      <th>Family_count</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Braund, Mr. Owen Harris</td>\n",
              "      <td>male</td>\n",
              "      <td>22.0</td>\n",
              "      <td>A/5 21171</td>\n",
              "      <td>7.2500</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
              "      <td>female</td>\n",
              "      <td>38.0</td>\n",
              "      <td>PC 17599</td>\n",
              "      <td>71.2833</td>\n",
              "      <td>C85</td>\n",
              "      <td>C</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>Heikkinen, Miss. Laina</td>\n",
              "      <td>female</td>\n",
              "      <td>26.0</td>\n",
              "      <td>STON/O2. 3101282</td>\n",
              "      <td>7.9250</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
              "      <td>female</td>\n",
              "      <td>35.0</td>\n",
              "      <td>113803</td>\n",
              "      <td>53.1000</td>\n",
              "      <td>C123</td>\n",
              "      <td>S</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Allen, Mr. William Henry</td>\n",
              "      <td>male</td>\n",
              "      <td>35.0</td>\n",
              "      <td>373450</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-9508c436-35f4-4f62-af4b-36b2f568bce5')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-9508c436-35f4-4f62-af4b-36b2f568bce5 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-9508c436-35f4-4f62-af4b-36b2f568bce5');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "   Survived  Pclass  ... Embarked Family_count\n",
              "0         0       3  ...        S            1\n",
              "1         1       1  ...        C            1\n",
              "2         1       3  ...        S            0\n",
              "3         1       1  ...        S            1\n",
              "4         0       3  ...        S            0\n",
              "\n",
              "[5 rows x 10 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Save the data\n",
        "titanic.to_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/titanic_clean.csv', index=False)"
      ],
      "metadata": {
        "id": "RsdUzqa3MnQc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Binary Cabin Index\n",
        "titanic['Cabin_index'] = np.where(titanic['Cabin'].isnull(), 0, 1)"
      ],
      "metadata": {
        "id": "RJ66XgyfNeka"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Sex -> Numeric\n",
        "sex_numeric = {'male': 0, 'female':1}\n",
        "titanic['Sex'] = titanic['Sex'].map(sex_numeric)"
      ],
      "metadata": {
        "id": "s0E-ttWBMS0H"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# More Cleaning\n",
        "titanic.drop(['Cabin', 'Embarked', 'Name', 'Ticket'], axis=1, inplace=True)\n",
        "titanic.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "2-hpDvaGMict",
        "outputId": "aef66829-30dc-4ae6-abda-ff322e73b628"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-76f3a8e0-72f5-40e8-96f8-3ab2a43c3c68\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Survived</th>\n",
              "      <th>Pclass</th>\n",
              "      <th>Sex</th>\n",
              "      <th>Age</th>\n",
              "      <th>Fare</th>\n",
              "      <th>Family_count</th>\n",
              "      <th>Cabin_index</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>22.0</td>\n",
              "      <td>7.2500</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>38.0</td>\n",
              "      <td>71.2833</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>26.0</td>\n",
              "      <td>7.9250</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>35.0</td>\n",
              "      <td>53.1000</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>35.0</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-76f3a8e0-72f5-40e8-96f8-3ab2a43c3c68')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-76f3a8e0-72f5-40e8-96f8-3ab2a43c3c68 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-76f3a8e0-72f5-40e8-96f8-3ab2a43c3c68');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "   Survived  Pclass  Sex   Age     Fare  Family_count  Cabin_index\n",
              "0         0       3    0  22.0   7.2500             1            0\n",
              "1         1       1    1  38.0  71.2833             1            1\n",
              "2         1       3    1  26.0   7.9250             0            0\n",
              "3         1       1    1  35.0  53.1000             1            1\n",
              "4         0       3    0  35.0   8.0500             0            0"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Save the data\n",
        "titanic.to_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/titanic_clean.csv', index=False)"
      ],
      "metadata": {
        "id": "guSLZfMYOZll"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "titanic = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/titanic_clean.csv')\n",
        "titanic.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "5GKD4d4iPGXj",
        "outputId": "eb7e5989-e91d-4c0c-d219-5aecf9161775"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "\n",
              "  <div id=\"df-fbfd27fa-3b0a-4a42-8fb1-4aa0e38b607a\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Survived</th>\n",
              "      <th>Pclass</th>\n",
              "      <th>Sex</th>\n",
              "      <th>Age</th>\n",
              "      <th>Fare</th>\n",
              "      <th>Family_count</th>\n",
              "      <th>Cabin_index</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>22.0</td>\n",
              "      <td>7.2500</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>38.0</td>\n",
              "      <td>71.2833</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>26.0</td>\n",
              "      <td>7.9250</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>35.0</td>\n",
              "      <td>53.1000</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>35.0</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-fbfd27fa-3b0a-4a42-8fb1-4aa0e38b607a')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-fbfd27fa-3b0a-4a42-8fb1-4aa0e38b607a button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-fbfd27fa-3b0a-4a42-8fb1-4aa0e38b607a');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ],
            "text/plain": [
              "   Survived  Pclass  Sex   Age     Fare  Family_count  Cabin_index\n",
              "0         0       3    0  22.0   7.2500             1            0\n",
              "1         1       1    1  38.0  71.2833             1            1\n",
              "2         1       3    1  26.0   7.9250             0            0\n",
              "3         1       1    1  35.0  53.1000             1            1\n",
              "4         0       3    0  35.0   8.0500             0            0"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Train Test Split\n",
        "features = titanic.drop('Survived', axis=1)\n",
        "labels = titanic['Survived']\n",
        "\n",
        "X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.4, random_state=42)\n",
        "X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.5, random_state=42)"
      ],
      "metadata": {
        "id": "BkO9L8dnPlcY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for data in [y_train, y_val, y_test]:\n",
        "  print(round(len(data) / len(labels), 2))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UOBy6SzHdOMo",
        "outputId": "d8972d53-1d73-4bed-85ee-93083657c2c5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0.6\n",
            "0.2\n",
            "0.2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Save the data\n",
        "X_train.to_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/train_features.csv', index=False)\n",
        "X_val.to_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/val_features.csv', index=False)\n",
        "X_test.to_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/test_features.csv', index=False)\n",
        "\n",
        "y_train.to_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/train_labels.csv', index=False)\n",
        "y_val.to_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/val_labels.csv', index=False)\n",
        "y_test.to_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/test_labels.csv', index=False)"
      ],
      "metadata": {
        "id": "6U5Yyh9ldiHN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Cross Validation"
      ],
      "metadata": {
        "id": "T2J1f-vZfykL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "train_features = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/train_features.csv')\n",
        "train_labels = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/train_labels.csv')\n",
        "\n",
        "val_features = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/val_features.csv')\n",
        "val_labels = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/val_labels.csv')\n",
        "\n",
        "test_features = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/test_features.csv')\n",
        "test_labels = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/IntroductionToML/Data/TitanicDataset/test_labels.csv')"
      ],
      "metadata": {
        "id": "-Qy59AcKfg4K"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "rf = RandomForestClassifier()\n",
        "\n",
        "scores = cross_val_score(rf, train_features, train_labels.values.ravel(), cv=5)"
      ],
      "metadata": {
        "id": "I5kCQCgJf1hW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "scores"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mIPQ5xkAlO9C",
        "outputId": "58aa841a-449c-43ca-cf10-2bbacddec0f1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([0.8317757 , 0.8317757 , 0.80373832, 0.80373832, 0.83018868])"
            ]
          },
          "metadata": {},
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Hyperparameter Tuning"
      ],
      "metadata": {
        "id": "GPmqkt-N2VKm"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "rf = RandomForestClassifier()\n",
        "\n",
        "hyperparams = {\n",
        "    'n_estimators': [5, 25, 50, 100],\n",
        "    'max_depth': [2, 12, 24, None]\n",
        "}\n",
        "\n",
        "cross_val = GridSearchCV(rf, hyperparams, cv=5)\n",
        "cross_val.fit(train_features, train_labels.values.ravel())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "95FLv5vamVXU",
        "outputId": "f156ef32-5396-4673-c5bd-4d5eac19b188"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "GridSearchCV(cv=5, estimator=RandomForestClassifier(),\n",
              "             param_grid={'max_depth': [2, 12, 24, None],\n",
              "                         'n_estimators': [5, 25, 50, 100]})"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def results(results):\n",
        "  print('Optimal Hyperparams: {}\\n'.format(results.best_params_))\n",
        "  means = results.cv_results_['mean_test_score']\n",
        "  stds = results.cv_results_['std_test_score']\n",
        "\n",
        "  for mean, std, params in zip(means, stds, results.cv_results_['params']):\n",
        "    print('Mean {} Standard Deviation {} Hyperparameters {}'.format(round(mean,3), round(std * 2, 3), params))"
      ],
      "metadata": {
        "id": "X0hbtvZl47Dz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "results(cross_val)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pWPzTYTA6gTA",
        "outputId": "f64f500d-29ea-4408-9f72-9d09dd06737e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Optimal Hyperparams: {'max_depth': 24, 'n_estimators': 5}\n",
            "\n",
            "Mean 0.785 Standard Deviation 0.078 Hyperparameters {'max_depth': 2, 'n_estimators': 5}\n",
            "Mean 0.796 Standard Deviation 0.11 Hyperparameters {'max_depth': 2, 'n_estimators': 25}\n",
            "Mean 0.787 Standard Deviation 0.116 Hyperparameters {'max_depth': 2, 'n_estimators': 50}\n",
            "Mean 0.802 Standard Deviation 0.119 Hyperparameters {'max_depth': 2, 'n_estimators': 100}\n",
            "Mean 0.811 Standard Deviation 0.053 Hyperparameters {'max_depth': 12, 'n_estimators': 5}\n",
            "Mean 0.824 Standard Deviation 0.057 Hyperparameters {'max_depth': 12, 'n_estimators': 25}\n",
            "Mean 0.817 Standard Deviation 0.03 Hyperparameters {'max_depth': 12, 'n_estimators': 50}\n",
            "Mean 0.817 Standard Deviation 0.034 Hyperparameters {'max_depth': 12, 'n_estimators': 100}\n",
            "Mean 0.826 Standard Deviation 0.056 Hyperparameters {'max_depth': 24, 'n_estimators': 5}\n",
            "Mean 0.811 Standard Deviation 0.047 Hyperparameters {'max_depth': 24, 'n_estimators': 25}\n",
            "Mean 0.813 Standard Deviation 0.032 Hyperparameters {'max_depth': 24, 'n_estimators': 50}\n",
            "Mean 0.813 Standard Deviation 0.033 Hyperparameters {'max_depth': 24, 'n_estimators': 100}\n",
            "Mean 0.811 Standard Deviation 0.055 Hyperparameters {'max_depth': None, 'n_estimators': 5}\n",
            "Mean 0.8 Standard Deviation 0.035 Hyperparameters {'max_depth': None, 'n_estimators': 25}\n",
            "Mean 0.813 Standard Deviation 0.037 Hyperparameters {'max_depth': None, 'n_estimators': 50}\n",
            "Mean 0.817 Standard Deviation 0.025 Hyperparameters {'max_depth': None, 'n_estimators': 100}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "rf1 = RandomForestClassifier(n_estimators=50, max_depth=12)\n",
        "rf1.fit(train_features, train_labels.values.ravel())\n",
        "\n",
        "rf2 = RandomForestClassifier(n_estimators=100, max_depth=12)\n",
        "rf2.fit(train_features, train_labels.values.ravel())\n",
        "\n",
        "rf3 = RandomForestClassifier(n_estimators=50, max_depth=None)\n",
        "rf3.fit(train_features, train_labels.values.ravel())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vYnwInCNB_DE",
        "outputId": "26ec6cb4-79ae-4df6-e44a-7adfeb2f0c1f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "RandomForestClassifier(n_estimators=50)"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Model Evaluation"
      ],
      "metadata": {
        "id": "IB-cb9KSDQPf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for mdl in [rf1, rf2, rf3]:\n",
        "  y_pred = mdl.predict(val_features)\n",
        "  accuracy = round(accuracy_score(val_labels, y_pred), 3)\n",
        "  precision = round(precision_score(val_labels, y_pred), 3)\n",
        "  recall = round(recall_score(val_labels, y_pred), 3)\n",
        "\n",
        "  print('Max Depth: {} || Estimators: {} || Accuracy: {} || Precision: {} || Recall: {}'.format(mdl.max_depth,\n",
        "                                                                                                mdl.n_estimators,\n",
        "                                                                                                accuracy,\n",
        "                                                                                                precision,\n",
        "                                                                                                recall))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qTpqyg_NDOcu",
        "outputId": "9dafa15c-b764-4ea3-8caf-52996ec7dc78"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Max Depth: 12 || Estimators: 50 || Accuracy: 0.827 || Precision: 0.836 || Recall: 0.737\n",
            "Max Depth: 12 || Estimators: 100 || Accuracy: 0.816 || Precision: 0.831 || Recall: 0.711\n",
            "Max Depth: None || Estimators: 50 || Accuracy: 0.816 || Precision: 0.812 || Recall: 0.737\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = rf1.predict(test_features)\n",
        "accuracy = round(accuracy_score(test_labels, y_pred), 3)\n",
        "precision = round(precision_score(test_labels, y_pred), 3)\n",
        "recall = round(recall_score(test_labels, y_pred), 3)\n",
        "\n",
        "print('Max Depth: {} || Estimators: {} || Accuracy: {} || Precision: {} || Recall: {}'.format(rf1.max_depth,\n",
        "                                                                                                rf1.n_estimators,\n",
        "                                                                                                accuracy,\n",
        "                                                                                                precision,\n",
        "                                                                                                recall))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vGEpDE7TOC4c",
        "outputId": "46e0bbf9-d94e-42b1-8c2e-42f43776f8fd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Max Depth: 12 || Estimators: 50 || Accuracy: 0.792 || Precision: 0.741 || Recall: 0.662\n"
          ]
        }
      ]
    }
  ]
}
