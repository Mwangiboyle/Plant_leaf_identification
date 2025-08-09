import uvicorn
from fastapi import FastAPI

label_map = {
    0: "bosement bamboo",
    1: "Chinese horse chestnut",
    2: "Anhui Barberry",
    3: "Chinese redbud",
    4: "true indigo",
    5: "Japanese maple",
    6: "Nanmu",
    7: "castor aralia",
    8: "camphor tree",
    9: "deodar",
    10: "big-fruited holly",
    11: "Japanese cheesewood",
    12: "cornelian cherry",
    13: "Japanese elm",
    14: "sweet osmanthus",
    15: "cedar of Lebanon",
    16: "ginkgo, maidenhair tree",
    17: "Crêpe myrtle, Crepe myrtle",
    18: "oleander",
    19: "podocarpus",
    20: "Japanese flowering cherry",
    21: "glossy privet",
    22: "Chinese toon",
    23: "peach",
    24: "Ford woodlotus",
    25: "bentham maple",
    26: "Bael tree",
    27: "southern magnolia",
    28: "Canadian poplar",
    29: "Chinese tulip tree",
    30: "tangerine"
}


app = FastAPI(
    title="Wlcome to my fastapi ",
)

@app.get('/')
async def root():
    return {"Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port = 8000)


