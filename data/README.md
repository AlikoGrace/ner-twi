# Dataset for Twi Named Entity Recognition (NER)

This folder contains data used for training and evaluating a Named Entity Recognition (NER) model for the Twi language, with a focus on low-resource African NLP.

## 📁 Folder Structure

- `raw/`: Contains the original, unprocessed text scraped from publicly available sources.
- `processed/`: Contains annotated files in CoNLL format, suitable for training and evaluation.

## 📚 Data Source

The original text was scraped from [worldstories.org.uk](https://worldstories.org.uk/reader/kweku-anansi-and-his-new-wife/akan/490), which provides free, open-access folktales in different languages for educational purposes.
Additional sentences were extracted from the Akan folktale "Abɛn a ɛgyee Ananse nkwa no" found in the paper:
Akrofi, E. (2023). Akan Anansesɛm: Abɛn a ɛgyee Ananse nkwa no. Academia.edu.
https://www.academia.edu/96287748/Akan_Ananses%C9%9Bm_Ab%C9%9Bn_a_%C9%9Bgyee_Ananse_nkwa_no

## ✍️ Annotations

The data has been manually annotated using the following entity types:

- `PER` – Person names
- `LOC` – Locations (countries, cities, villages)
- `ORG` – Organizations (schools, institutions)
- `DATE` – Dates (days, years, etc.)

Annotations were created using [Label Studio](https://labelstud.io/) and exported in CoNLL-2003 format.

## ⚠️ Licensing and Use

This dataset is created for educational and research purposes only. Please cite this repository or link back if using or building on the dataset.

## 🤝 Contribute

If you'd like to contribute additional annotated sentences in Twi (or Ewe), feel free to open a pull request or contact the maintainer.

---
