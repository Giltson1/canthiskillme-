# Project Plan

## Goal
Calling a poisonous mushroom edible is much worse than the other way around. So what we train the model to predict matters.

**Question:** Does a CNN that predicts the *species* (then we look up if that species is poisonous) miss fewer poisonous mushrooms than the same CNN trained to predict *poisonous vs. edible* directly?

**What we expect:** We think the species model will catch more poisonous mushrooms. Some poisonous and edible species look very alike, and learning each species should help the model see the small differences. If the direct model wins, then the extra species detail doesn't help for a yes/no decision.

## Connection to literature
- **DF20 [1]:** where our dataset comes from. It also gives CNN results on DF20-Mini we can compare to.
- **ResNet [3]:** the model we use for both versions.

## Data
- **DF20-Mini:** 36,393 expert-labeled photos, 182 species, six genera [1].
- **Poisonous labels:** from the FungiCLEF species list [2], [4].
- **Split:** 70% train / 15% validation / 15% test. We split by *observation* (one mushroom can have several photos), so the same mushroom is never in both train and test.

## Methods
Same ResNet-18 [3] (pretrained on ImageNet) and same settings for both. Only the target changes.

| Model | Predicts | How we decide "poisonous" |
|---|---|---|
| A — species | 182 species | look up the predicted species |
| B — direct | poisonous or not | model output |
| Baseline | nothing | always say "not poisonous" |

## Evaluation
- **Main metric:** recall on poisonous mushrooms (how many we catch) on the test set.
- **Also:** precision on poisonous and overall accuracy.
- Each model runs 3 times with different seeds, and we average.
- If A's recall is clearly higher than B's, species training helps. If they're close, it doesn't matter much.

## Compute
Free Google Colab GPU. About 1–1.5 hours per run, 6 runs total, so around 6–9 hours.

## Timeline
- **Checkpoint:** data downloaded, labels and split done, one run of A and B finished.
- **Poster draft:** all runs done, results table and plots ready.

## Fallback
- Colab too slow: use smaller images or fewer runs.
- Some species missing a poisonous label: drop them.
- A and B tie: try making B favor "poisonous" more and see if recall goes up.

## Disclaimer
This is a class project, not a guide to what is safe to eat.

# Download the dataset
```bash
wget http://ptak.felk.cvut.cz/plants/DanishFungiDataset/DF20M-images.tar.gz
wget http://ptak.felk.cvut.cz/plants/DanishFungiDataset/DF20M-metadata.zip
tar -xzf DF20M-images.tar.gz && unzip DF20M-metadata.zip
```