# Text2Image Search System

## Overview
This repository contains the code for a Text2Image Search system, allowing users to search for images based on textual queries. The system is built using the Haystack library and leverages multimodal retrievers to handle both text and image data. The implementation involves the creation of embeddings for both textual and image data, enabling efficient retrieval of relevant images based on user queries.

## System Architecture
**1. Data Collection and Preparation**
The dataset consists of 178 images manually collected from three distinct categories: animals, flowers, and fashion. Each category has specific classes such as zebra, rose, black cat, jeans, and jackets. Images are stored in the "Data" directory.

**2. Document Store**
An InMemoryDocumentStore is employed to store document embeddings. The embeddings have a dimensionality of 512. Images are represented as documents with their paths as content and content type set to "image." These documents are then written to the document store.

**3. Retrieval Models**
The system uses the MultiModalRetriever from Haystack, which allows the integration of both textual and image embeddings. For text embedding, the "sentence-transformers/clip-ViT-B-32" model is used, while the same model is employed for image embeddings. This enables a seamless combination of textual and image data during the retrieval process.

**4. Search Pipeline**
A search pipeline is created using the Pipeline class from Haystack. The pipeline includes a single node - the multimodal retriever (retriever_text_to_image). The pipeline is responsible for handling user queries and returning relevant search results.

**5. User Interface (Streamlit App)**
The user interface is implemented using Streamlit. Users can input queries through a text input field and initiate searches. The top-k search results are then displayed, along with their respective scores and images.

## Techniques Employed
- **Multimodal Retrieval**: The system leverages multimodal retrieval techniques to handle both text and image data, providing a unified search experience.
- **Embedding Models**: The "sentence-transformers/clip-ViT-B-32" model is used for generating embeddings for both text and images, facilitating efficient comparison and retrieval.
- **Streamlit for UI**: Streamlit is employed to create a user-friendly interface for interacting with the Text2Image search system.

## Challenges Encountered
- **Version Incompatibility Issues**: One major challenge faced during implementation was version incompatibility issues. Ensuring compatibility between different library versions, especially for Haystack and Streamlit, required careful consideration and adjustment of dependencies.
- **Data Collection and Diversity**: Manually collecting and curating a diverse dataset posed a challenge. Ensuring that each category has a representative set of classes and images was crucial for the system's performance and generalizability.

## Instructions for Running the System
1. Install dependencies
```bash
pip install -r requirements.txt.
```
2. Run the app.py
```bash
streamlit run app.py.
```
3. Access the Text2Image Search App through the provided local URL.


## Potential Avenues for Improvement
### Handling No Match Scenarios 
**Challenge**: One notable issue in the current system is its response when a text query does not match any image in the dataset. In such cases, the model might return an image that it deems to have similar features, leading to potentially misleading results. 

**Solution**: 
1. **Confidence Thresholding:** Set a confidence threshold; if the top-ranked result falls below it, convey to the user that no matching images were found.
2. **Negative Samples:** Train the model with negative samples to better distinguish instances where queries shouldn't yield relevant images.
3. **User Feedback Integration:** Allow user feedback to enhance the model by incorporating user input on result relevance.

### Diversity and Generalization
**Challenge**: Ensuring diversity and generalization in the dataset is crucial for the model's performance. The current system relies on a manually curated dataset, which may not cover all possible scenarios.

**Solutions:**
1. **Data Augmentation:** Apply techniques like random rotations and flips to augment the dataset artificially.
2. **Dynamic Dataset Expansion:** Dynamically expand the dataset based on user interactions and fetch relevant images from external sources.
3. **Incorporate External Knowledge:** Integrate external knowledge sources, like image databases, for additional context and improved retrieval.

By implementing these enhancements, the Text2Image Search system can offer more accurate results and better adapt to diverse user queries over time. Continuous user feedback and monitoring will be integral for ongoing system refinement.


## Sample Images

![Sample-1](https://github.com/VivekSai07/Text2Image-Search-System/blob/main/Sample-1.png)
![Sample-2](https://github.com/VivekSai07/Text2Image-Search-System/blob/main/Sample-2.png)
![Sample-3](https://github.com/VivekSai07/Text2Image-Search-System/blob/main/Sample-3.png)
