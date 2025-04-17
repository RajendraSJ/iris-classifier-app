{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b31bcfab-3d29-4278-865d-f53d8bc4e365",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-17 20:15:00.095 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run D:\\Anaconda\\Files\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-04-17 20:15:00.107 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "from sklearn.datasets import load_iris\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "\n",
    "# Load data\n",
    "iris = load_iris()\n",
    "X = iris.data\n",
    "y = iris.target\n",
    "\n",
    "# Train model\n",
    "model = RandomForestClassifier()\n",
    "model.fit(X, y)\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"Iris Flower Classifier 🌸\")\n",
    "sepal_length = st.slider(\"Sepal Length\", float(X[:,0].min()), float(X[:,0].max()))\n",
    "sepal_width = st.slider(\"Sepal Width\", float(X[:,1].min()), float(X[:,1].max()))\n",
    "petal_length = st.slider(\"Petal Length\", float(X[:,2].min()), float(X[:,2].max()))\n",
    "petal_width = st.slider(\"Petal Width\", float(X[:,3].min()), float(X[:,3].max()))\n",
    "\n",
    "input_data = [[sepal_length, sepal_width, petal_length, petal_width]]\n",
    "prediction = model.predict(input_data)\n",
    "\n",
    "st.write(f\"### Prediction: {iris.target_names[prediction][0]}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "fdb65d80-6123-41ec-9939-598440e4ece6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
