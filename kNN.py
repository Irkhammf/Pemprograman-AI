{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Tupro4_Kel1_MobilRank",
      "provenance": [],
      "collapsed_sections": [],
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
        "<a href=\"https://colab.research.google.com/github/Irkhammf/Tugas-Pemprograman-AI/blob/main/kNN.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jc6ExVxyPXKI"
      },
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6zy44jF2P7be"
      },
      "source": [
        "#Membaca file excel\n",
        "def data_excel(data):\n",
        "    xls = pd.read_excel(data)\n",
        "    return xls"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 576
        },
        "id": "xo64Y8ghQDEM",
        "outputId": "36f06517-2f2e-4052-c000-bc9be40d7389"
      },
      "source": [
        "#Memasukkan data excel ke dalam variabel\n",
        "df = data_excel('mobil.xls')\n",
        "df"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
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
              "      <th>Nama Mobil</th>\n",
              "      <th>Ukuran</th>\n",
              "      <th>Kenyamanan</th>\n",
              "      <th>Irit</th>\n",
              "      <th>Kecepatan</th>\n",
              "      <th>Harga (Ratus Juta)</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Toyota Agya</td>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>9</td>\n",
              "      <td>6</td>\n",
              "      <td>1.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Daihatsu Alya</td>\n",
              "      <td>4</td>\n",
              "      <td>3</td>\n",
              "      <td>9</td>\n",
              "      <td>6</td>\n",
              "      <td>1.10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Toyota Avanza</td>\n",
              "      <td>6</td>\n",
              "      <td>5</td>\n",
              "      <td>6</td>\n",
              "      <td>6</td>\n",
              "      <td>2.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Daihatsu Xenia</td>\n",
              "      <td>6</td>\n",
              "      <td>4</td>\n",
              "      <td>6</td>\n",
              "      <td>6</td>\n",
              "      <td>1.75</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Xpander</td>\n",
              "      <td>7</td>\n",
              "      <td>7</td>\n",
              "      <td>6</td>\n",
              "      <td>7</td>\n",
              "      <td>2.25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>Livina</td>\n",
              "      <td>7</td>\n",
              "      <td>7</td>\n",
              "      <td>6</td>\n",
              "      <td>7</td>\n",
              "      <td>2.10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>Karimun</td>\n",
              "      <td>3</td>\n",
              "      <td>4</td>\n",
              "      <td>10</td>\n",
              "      <td>5</td>\n",
              "      <td>1.20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>Toyota Innova</td>\n",
              "      <td>8</td>\n",
              "      <td>8</td>\n",
              "      <td>5</td>\n",
              "      <td>7</td>\n",
              "      <td>4.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>Alphard</td>\n",
              "      <td>9</td>\n",
              "      <td>10</td>\n",
              "      <td>4</td>\n",
              "      <td>8</td>\n",
              "      <td>10.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>Toyota Vios</td>\n",
              "      <td>5</td>\n",
              "      <td>7</td>\n",
              "      <td>9</td>\n",
              "      <td>8</td>\n",
              "      <td>2.50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>Honda City</td>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>7</td>\n",
              "      <td>8</td>\n",
              "      <td>2.70</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>Toyota Hiace</td>\n",
              "      <td>10</td>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>6</td>\n",
              "      <td>5.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>Toyota Fortuner</td>\n",
              "      <td>9</td>\n",
              "      <td>8</td>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>5.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>Toyota Foxy</td>\n",
              "      <td>9</td>\n",
              "      <td>9</td>\n",
              "      <td>5</td>\n",
              "      <td>7</td>\n",
              "      <td>5.50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>Toyota Corolla Altis</td>\n",
              "      <td>5</td>\n",
              "      <td>9</td>\n",
              "      <td>7</td>\n",
              "      <td>9</td>\n",
              "      <td>6.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>Suzuki Ertiga</td>\n",
              "      <td>7</td>\n",
              "      <td>7</td>\n",
              "      <td>7</td>\n",
              "      <td>7</td>\n",
              "      <td>2.30</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>Suzuki Carry</td>\n",
              "      <td>7</td>\n",
              "      <td>3</td>\n",
              "      <td>9</td>\n",
              "      <td>5</td>\n",
              "      <td>0.80</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "              Nama Mobil  Ukuran  ...  Kecepatan  Harga (Ratus Juta)\n",
              "0            Toyota Agya       4  ...          6                1.00\n",
              "1          Daihatsu Alya       4  ...          6                1.10\n",
              "2          Toyota Avanza       6  ...          6                2.00\n",
              "3         Daihatsu Xenia       6  ...          6                1.75\n",
              "4                Xpander       7  ...          7                2.25\n",
              "5                 Livina       7  ...          7                2.10\n",
              "6                Karimun       3  ...          5                1.20\n",
              "7          Toyota Innova       8  ...          7                4.00\n",
              "8                Alphard       9  ...          8               10.00\n",
              "9            Toyota Vios       5  ...          8                2.50\n",
              "10            Honda City       5  ...          8                2.70\n",
              "11          Toyota Hiace      10  ...          6                5.00\n",
              "12       Toyota Fortuner       9  ...          8                5.00\n",
              "13           Toyota Foxy       9  ...          7                5.50\n",
              "14  Toyota Corolla Altis       5  ...          9                6.00\n",
              "15         Suzuki Ertiga       7  ...          7                2.30\n",
              "16          Suzuki Carry       7  ...          5                0.80\n",
              "\n",
              "[17 rows x 6 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 65
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G6aVDoYwQPg1",
        "outputId": "fc9e3cc6-e9a5-41f4-a1ca-b7f4c1859f98"
      },
      "source": [
        "df.info()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 17 entries, 0 to 16\n",
            "Data columns (total 6 columns):\n",
            " #   Column              Non-Null Count  Dtype  \n",
            "---  ------              --------------  -----  \n",
            " 0   Nama Mobil          17 non-null     object \n",
            " 1   Ukuran              17 non-null     int64  \n",
            " 2   Kenyamanan          17 non-null     int64  \n",
            " 3   Irit                17 non-null     int64  \n",
            " 4   Kecepatan           17 non-null     int64  \n",
            " 5   Harga (Ratus Juta)  17 non-null     float64\n",
            "dtypes: float64(1), int64(4), object(1)\n",
            "memory usage: 944.0+ bytes\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "OLfSSpc2XJ6K"
      },
      "source": [
        "df = df.rename({'Nama Mobil' : 'Name'}, axis=1)\n",
        "train = df.rename({'Harga (Ratus Juta)' : 'Harga'}, axis=1)\n",
        "train = train.drop('Name', axis=1)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 576
        },
        "id": "U26AYKlJHlmf",
        "outputId": "125efd5e-c925-4681-f6c1-554985dee0a3"
      },
      "source": [
        "#Data train (data yang sudah diclear sehingga hanya memiliki nilai integer dan float)\n",
        "train"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
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
              "      <th>Ukuran</th>\n",
              "      <th>Kenyamanan</th>\n",
              "      <th>Irit</th>\n",
              "      <th>Kecepatan</th>\n",
              "      <th>Harga</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>4</td>\n",
              "      <td>4</td>\n",
              "      <td>9</td>\n",
              "      <td>6</td>\n",
              "      <td>1.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>4</td>\n",
              "      <td>3</td>\n",
              "      <td>9</td>\n",
              "      <td>6</td>\n",
              "      <td>1.10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>6</td>\n",
              "      <td>5</td>\n",
              "      <td>6</td>\n",
              "      <td>6</td>\n",
              "      <td>2.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>6</td>\n",
              "      <td>4</td>\n",
              "      <td>6</td>\n",
              "      <td>6</td>\n",
              "      <td>1.75</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>7</td>\n",
              "      <td>7</td>\n",
              "      <td>6</td>\n",
              "      <td>7</td>\n",
              "      <td>2.25</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>7</td>\n",
              "      <td>7</td>\n",
              "      <td>6</td>\n",
              "      <td>7</td>\n",
              "      <td>2.10</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>3</td>\n",
              "      <td>4</td>\n",
              "      <td>10</td>\n",
              "      <td>5</td>\n",
              "      <td>1.20</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>8</td>\n",
              "      <td>8</td>\n",
              "      <td>5</td>\n",
              "      <td>7</td>\n",
              "      <td>4.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>9</td>\n",
              "      <td>10</td>\n",
              "      <td>4</td>\n",
              "      <td>8</td>\n",
              "      <td>10.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>5</td>\n",
              "      <td>7</td>\n",
              "      <td>9</td>\n",
              "      <td>8</td>\n",
              "      <td>2.50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>10</th>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>7</td>\n",
              "      <td>8</td>\n",
              "      <td>2.70</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>11</th>\n",
              "      <td>10</td>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>6</td>\n",
              "      <td>5.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>12</th>\n",
              "      <td>9</td>\n",
              "      <td>8</td>\n",
              "      <td>5</td>\n",
              "      <td>8</td>\n",
              "      <td>5.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>13</th>\n",
              "      <td>9</td>\n",
              "      <td>9</td>\n",
              "      <td>5</td>\n",
              "      <td>7</td>\n",
              "      <td>5.50</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>14</th>\n",
              "      <td>5</td>\n",
              "      <td>9</td>\n",
              "      <td>7</td>\n",
              "      <td>9</td>\n",
              "      <td>6.00</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>15</th>\n",
              "      <td>7</td>\n",
              "      <td>7</td>\n",
              "      <td>7</td>\n",
              "      <td>7</td>\n",
              "      <td>2.30</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>16</th>\n",
              "      <td>7</td>\n",
              "      <td>3</td>\n",
              "      <td>9</td>\n",
              "      <td>5</td>\n",
              "      <td>0.80</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "    Ukuran  Kenyamanan  Irit  Kecepatan  Harga\n",
              "0        4           4     9          6   1.00\n",
              "1        4           3     9          6   1.10\n",
              "2        6           5     6          6   2.00\n",
              "3        6           4     6          6   1.75\n",
              "4        7           7     6          7   2.25\n",
              "5        7           7     6          7   2.10\n",
              "6        3           4    10          5   1.20\n",
              "7        8           8     5          7   4.00\n",
              "8        9          10     4          8  10.00\n",
              "9        5           7     9          8   2.50\n",
              "10       5           8     7          8   2.70\n",
              "11      10           5     8          6   5.00\n",
              "12       9           8     5          8   5.00\n",
              "13       9           9     5          7   5.50\n",
              "14       5           9     7          9   6.00\n",
              "15       7           7     7          7   2.30\n",
              "16       7           3     9          5   0.80"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 68
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "z0uu6x77XhKl",
        "outputId": "eba19e6d-3bf0-405d-f5fa-659f9d028639"
      },
      "source": [
        "train.info()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 17 entries, 0 to 16\n",
            "Data columns (total 5 columns):\n",
            " #   Column      Non-Null Count  Dtype  \n",
            "---  ------      --------------  -----  \n",
            " 0   Ukuran      17 non-null     int64  \n",
            " 1   Kenyamanan  17 non-null     int64  \n",
            " 2   Irit        17 non-null     int64  \n",
            " 3   Kecepatan   17 non-null     int64  \n",
            " 4   Harga       17 non-null     float64\n",
            "dtypes: float64(1), int64(4)\n",
            "memory usage: 808.0 bytes\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YXaYyPU8V5wt"
      },
      "source": [
        "#Membangun data inputan yang bakal ditest\n",
        "def testData(data, tr) :\n",
        "    test = data.copy()\n",
        "    test['Ukuran'] = round(np.mean(tr['Ukuran']))\n",
        "    test['Kenyamanan'] = round(np.mean(tr['Kenyamanan']))\n",
        "    test['Irit'] = round(np.mean(tr['Irit']))\n",
        "    test['Kecepatan'] = round(np.mean(tr['Kecepatan']))\n",
        "    test['Harga'] = np.mean(tr['Harga'])\n",
        "    print(test)\n",
        "    return test"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "X07T9VJTY1x4",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "c2991109-1648-4711-9020-fccaaa9350a6"
      },
      "source": [
        "#Menampilkan data test\n",
        "test = testData(train.loc[0], train)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Ukuran        7.000000\n",
            "Kenyamanan    6.000000\n",
            "Irit          7.000000\n",
            "Kecepatan     7.000000\n",
            "Harga         3.247059\n",
            "Name: 0, dtype: float64\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "UTGU7BldMRY1"
      },
      "source": [
        "##Rumus kNN##"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Nbxf-4WLZiTd"
      },
      "source": [
        "def euclidian (trainData, testData):\n",
        "    return (((testData['Ukuran']- trainData['Ukuran'])**2) + ((testData['Kenyamanan']- trainData['Kenyamanan'])**2) + ((testData['Irit']- trainData['Irit'])**2) + ((testData['Kecepatan']- trainData['Kecepatan'])**2) + ((testData['Harga']- trainData['Harga'])**2))**(1/2)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "szWvTZ8oaZRv"
      },
      "source": [
        "def manhattan (trainData, testData):\n",
        "    return ((abs(testData['Ukuran']- trainData['Ukuran'])) + (abs(testData['Kenyamanan']- trainData['Kenyamanan'])) + (abs(testData['Irit']- trainData['Irit'])) + (abs(testData['Kecepatan']- trainData['Kecepatan'])) + (abs(testData['Harga']- trainData['Harga'])))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FORo0axkabxW"
      },
      "source": [
        "def minkowski (trainData, testData, h = 1.5):\n",
        "    return ((abs(testData['Ukuran']- trainData['Ukuran'])**h) + (abs(testData['Kenyamanan']- trainData['Kenyamanan'])**h) + (abs(testData['Irit']- trainData['Irit'])**h) + (abs(testData['Kecepatan']- trainData['Kecepatan'])**h) + (abs(testData['Harga']- trainData['Harga'])**h))**(1/h)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ioMI8aQZacQd"
      },
      "source": [
        "def supremum (trainData, testData):\n",
        "    tmp = []\n",
        "    tmp.append(abs(testData['Ukuran']- trainData['Ukuran']))\n",
        "    tmp.append(abs(testData['Kenyamanan']- trainData['Kenyamanan']))\n",
        "    tmp.append(abs(testData['Irit']- trainData['Irit']))\n",
        "    tmp.append(abs(testData['Kecepatan']- trainData['Kecepatan']))\n",
        "    tmp.append(abs(testData['Harga']- trainData['Harga']))\n",
        "    return max(tmp)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "kBOCo1RPd1iy"
      },
      "source": [
        "#Menghitung jarak dengan masing - masing rumus\n",
        "Jarak_Euclidian = []\n",
        "Jarak_Manhattan = []\n",
        "Jarak_Minkowski = []\n",
        "Jarak_Supremum = []\n",
        "\n",
        "for i in range(len(train)):\n",
        "    Jarak_Euclidian.append(euclidian(train.loc[i], test))\n",
        "    Jarak_Manhattan.append(manhattan(train.loc[i], test))\n",
        "    Jarak_Minkowski.append(minkowski(train.loc[i], test))\n",
        "    Jarak_Supremum.append(supremum(train.loc[i], test))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F86FZtDMj7Ps",
        "outputId": "1350da65-7858-4ea7-c0e2-fadbfe875e7c"
      },
      "source": [
        "#Menampilkan nilai jarak dari masing - masing rumus\n",
        "print(Jarak_Euclidian)\n",
        "print(Jarak_Manhattan)\n",
        "print(Jarak_Minkowski)\n",
        "print(Jarak_Supremum)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[4.800965877446056, 5.254508691751827, 2.3569377822383344, 3.039931762574164, 1.7303543849679617, 1.820918434372247, 6.09839731626184, 3.093043875412199, 8.694953394519834, 3.2493225272067328, 3.049470996156773, 3.882370766447493, 4.009090017468564, 4.698483153597199, 4.957689494220798, 1.377287339383076, 4.794590377270319]\n",
            "[10.24705882352941, 11.147058823529411, 5.247058823529411, 6.497058823529411, 2.997058823529411, 3.147058823529411, 13.047058823529412, 5.752941176470589, 16.75294117647059, 6.747058823529411, 5.547058823529411, 7.752941176470589, 8.75294117647059, 9.25294117647059, 9.75294117647059, 1.947058823529411, 9.44705882352941]\n",
            "[6.141902222187615, 6.7062479031246545, 3.075148999660582, 3.885896968892238, 2.078045525986723, 2.184412818820784, 7.799434522134326, 3.766628169657741, 10.612682969562565, 4.100226875194534, 3.680699772292616, 4.80022833168838, 5.184882565266834, 5.873505554423372, 6.195396242652687, 1.5456672429923253, 5.995650378195755]\n",
            "[3.0, 3.0, 1.2470588235294109, 2.0, 1.0, 1.1470588235294108, 4.0, 2.0, 6.752941176470589, 2.0, 2.0, 3.0, 2.0, 3.0, 3.0, 1.0, 3.0]\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FykaCIPfMgQi"
      },
      "source": [
        "##Data Analisis##"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "q7JNdvYltMvp",
        "outputId": "3c9c1cff-bb16-466a-bb50-81a1a6d05380"
      },
      "source": [
        "#Euclidian\n",
        "plt.bar(range(len(Jarak_Euclidian)), Jarak_Euclidian)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<BarContainer object of 17 artists>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 79
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "3k6DEaIztUQU",
        "outputId": "d97a41a5-8fa1-49c1-8adb-732331c8136c"
      },
      "source": [
        "#Manhattan\n",
        "plt.bar(range(len(Jarak_Manhattan)), Jarak_Manhattan)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<BarContainer object of 17 artists>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 80
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 282
        },
        "id": "OZ8YjN0dtVXx",
        "outputId": "af0cdbc9-4f1f-4c6c-b69f-b233629a8245"
      },
      "source": [
        "#Minkowski\n",
        "plt.bar(range(len(Jarak_Minkowski)), Jarak_Minkowski)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<BarContainer object of 17 artists>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 81
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 284
        },
        "id": "R2LjGTJWtVse",
        "outputId": "47456c95-4646-4248-a5d8-b668bf66e8b7"
      },
      "source": [
        "#Supremum\n",
        "plt.bar(range(len(Jarak_Supremum)), Jarak_Supremum)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<BarContainer object of 17 artists>"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 82
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "tags": [],
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4j-ud5DTRjpO"
      },
      "source": [
        "#Mencari kelas mobil dominan dari 3 mobil terrekomendasi\n",
        "def prediksi(mobil):\n",
        "    domClass = [0, 0, 0, 0, 0, 0, 0, 0]\n",
        "    for i in range(len(mobil)):\n",
        "        if mobil[i][0] == 'H' and mobil[i][4] == 'a':\n",
        "            domClass[0]+=1\n",
        "        elif mobil[i][0] == 'T' and mobil[i][5] == 'a':\n",
        "            domClass[1]+=1\n",
        "        elif mobil[i][0] == 'S' and mobil[i][5] == 'i':\n",
        "            domClass[2]+=1\n",
        "        elif mobil[i][0] == 'L' and mobil[i][5] == 'a':\n",
        "            domClass[3]+=1\n",
        "        elif mobil[i][0] == 'X' and mobil[i][6] == 'r':\n",
        "            domClass[4]+=1\n",
        "        elif mobil[i][0] == 'K' and mobil[i][6] == 'n':\n",
        "            domClass[5]+=1\n",
        "        elif mobil[i][0] == 'A' and mobil[i][6] == 'd':\n",
        "            domClass[6]+=1\n",
        "        else:\n",
        "            domClass[7]+=1\n",
        "    return domClass"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "GB-kAn1FWCy-"
      },
      "source": [
        "#Menampilkan kelas dari data yang ditest\n",
        "def class_test(pred):\n",
        "    if max(pred) == 1:\n",
        "        print('Mobil unik/tidak termasuk dalam kelas yang ada')\n",
        "    elif max(pred) == pred[0]:\n",
        "        print('Mobil termasuk kelas Honda')\n",
        "    elif max(pred) == pred[1]:\n",
        "        print('Mobil termasuk kelas Toyota')\n",
        "    elif max(pred) == pred[2]:\n",
        "        print('Mobil termasuk kelas Suzuki')\n",
        "    elif max(pred) == pred[3]:\n",
        "        print('Mobil termasuk kelas Livina')\n",
        "    elif max(pred) == pred[4]:\n",
        "        print('Mobil termasuk kelas Xpander')\n",
        "    elif max(pred) == pred[5]:\n",
        "        print('Mobil termasuk kelas Karimun')\n",
        "    elif max(pred) == pred[6]:\n",
        "        print('Mobil termasuk kelas Alphard')\n",
        "    elif max(pred) == pred[7]:\n",
        "        print('Mobil termasuk kelas Daihatsu')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eO3JVj8TQ78T"
      },
      "source": [
        "#Honda = 1\n",
        "#Toyota = 2\n",
        "#Suzuki = 3\n",
        "#Livina = 4\n",
        "#Xpander = 5\n",
        "#Karimun = 6\n",
        "#Alphard = 7\n",
        "#Daihatsu = 8"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "xM28jlDKuUsT"
      },
      "source": [
        "#3 Jarak terdekat menggunakan masing - masing rumus jarak\n",
        "def terdekat(jarak):\n",
        "    result = []\n",
        "    mobil = []\n",
        "    best = sorted(jarak)\n",
        "    tmp = []\n",
        "    marked = []\n",
        "    bestCar = []\n",
        "    for i in range(3):\n",
        "        for j in range(len(jarak)):\n",
        "            if best[i] == jarak[j] and j not in marked:\n",
        "                bestCar.append(df.loc[j].Name)\n",
        "                result.append(best[i])\n",
        "                marked.append(j)\n",
        "                if len(result) == 3:\n",
        "                    return result, bestCar"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "S2BhmmToNBCx"
      },
      "source": [
        "##Main##"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HMex-1uMV47A"
      },
      "source": [
        "hasil, mobil_terbaik = terdekat(Jarak_Minkowski)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 102
        },
        "id": "4sUi1RMr1gF7",
        "outputId": "76094d5e-0086-472e-822a-fbbfd35b52c0"
      },
      "source": [
        "bestValue = sorted(zip(mobil_terbaik, hasil), key=lambda x:x[1], reverse=False)\n",
        "display(bestValue)\n",
        "prediksi_Class = prediksi(mobil_terbaik)\n",
        "print(prediksi_Class)\n",
        "class_test(prediksi_Class)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "[('Suzuki Ertiga', 1.5456672429923253),\n",
              " ('Xpander', 2.078045525986723),\n",
              " ('Livina', 2.184412818820784)]"
            ]
          },
          "metadata": {
            "tags": []
          }
        },
        {
          "output_type": "stream",
          "text": [
            "[0, 0, 1, 1, 1, 0, 0, 0]\n",
            "Mobil unik/tidak termasuk dalam kelas yang ada\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 85
        },
        "id": "GRliJWyr1O0v",
        "outputId": "09e0c40f-6e38-48d2-b749-f250bb91e49d"
      },
      "source": [
        "mobil_Terrekomendasi = [('Nama Mobil', 'Jarak')]\n",
        "for i in range(len(bestValue)) :\n",
        "    mobil_Terrekomendasi.append(bestValue[i])\n",
        "display(mobil_Terrekomendasi)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "[('Nama Mobil', 'Jarak'),\n",
              " ('Suzuki Ertiga', 1.5456672429923253),\n",
              " ('Xpander', 2.078045525986723),\n",
              " ('Livina', 2.184412818820784)]"
            ]
          },
          "metadata": {
            "tags": []
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "bzH_B3-L1JH9"
      },
      "source": [
        "#Melakukan output file rekomendasi.xls yang berisi 3 mobil terrekomendasi\n",
        "pd.DataFrame(mobil_Terrekomendasi).to_excel('rekomendasi.xls', header=False, index=False)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HG3__ZQG289l"
      },
      "source": [
        "rekomendasi = pd.read_excel('rekomendasi.xls')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 142
        },
        "id": "IqNHpUo_3FXc",
        "outputId": "95dfd8ff-55d0-42c1-9716-65e2efb1f686"
      },
      "source": [
        "rekomendasi"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
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
              "      <th>Nama Mobil</th>\n",
              "      <th>Jarak</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>Suzuki Ertiga</td>\n",
              "      <td>1.545667</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Xpander</td>\n",
              "      <td>2.078046</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Livina</td>\n",
              "      <td>2.184413</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "      Nama Mobil     Jarak\n",
              "0  Suzuki Ertiga  1.545667\n",
              "1        Xpander  2.078046\n",
              "2         Livina  2.184413"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 93
        }
      ]
    }
  ]
}