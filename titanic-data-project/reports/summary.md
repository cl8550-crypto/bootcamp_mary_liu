{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "98acf202-f288-4835-a49b-3941b5520a7f",
   "metadata": {},
   "source": [
    "cat > reports/summary.md << 'EOF'\n",
    "# Titanic Survival Prediction — Stakeholder Report\n",
    "\n",
    "## Executive Summary\n",
    "We built a simple logistic regression model to predict Titanic survival.\n",
    "Key drivers: Sex (females higher survival), Passenger Class (1st class higher), and Family presence.\n",
    "\n",
    "## Results\n",
    "- Accuracy ~80%\n",
    "- Robust to outliers\n",
    "- FamilySize and IsAlone add small signal\n",
    "\n",
    "## Assumptions & Risks\n",
    "- Age filled with median\n",
    "- Outliers flagged but not dropped\n",
    "- Logistic regression assumes linear log-odds\n",
    "\n",
    "## Recommendations\n",
    "- Use as teaching/demo model\n",
    "- Not reliable for critical safety planning\n",
    "EOF\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "50cab695-8a18-4ba7-9fdc-93abb2dbffe9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (fe-course)",
   "language": "python",
   "name": "fe-course"
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
   "version": "3.11.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
