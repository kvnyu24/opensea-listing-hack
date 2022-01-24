from utils.snipe import collection_map, pipeline 
import pandas as pd

def sort_data(collection):
    df = pd.read_csv(collection_map[collection]["orders"]).sort_values(by=["price"])

    print(df.head(10))

if __name__ == '__main__':
    # Collect all the data

    # pipeline("Meebits", 6562)
    # pipeline("Azuki", 5723)
    # pipeline("CryptoCoven", 6826)
    # pipeline("WoW", 5522)
    # pipeline("Doodle", 5850)
    # pipeline("BAYC", 7275)

    # Sort & present simple analytics
    # sort_data("BAYC")
    # sort_data("Meebits")
    # sort_data("Azuki")
    # sort_data("CryptoCoven")
    # sort_data("WoW")
    sort_data("Doodle")
