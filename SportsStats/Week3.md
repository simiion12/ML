# Milestone 3: Beyond DEscriptive Stats 
## Dive Deeper
   
In this phase, I plan to delve into exploring the relationships between variables that were previously overlooked. To achieve this, I will utilize Pearson's correlation coefficient, complemented by visualizing a heatmap to illustrate the relationships between various features.

The heatmap shows a particularly strong correlation between Weight and Height, marked at 0.8, suggesting a significant positive relationship, which is logical as taller individuals tend to weigh more.  correlation between Year and other features is mostly weak, indicating that the features do not have a strong linear relationship with the year. Other relationships between the variables appear less pronounced as well there are no strong negative correlations observed in the dataset.
<p align="center">
  <img src="https://github.com/russian17/ML/assets/120457811/6a0a9045-e03d-40a1-90b0-f7d5ca30605f" />
</p>

## New Metric

After reviewing the correlation heatmap, which highlighted a significant correlation between Weight and Height, I've elected to introduce a new metric: the Body Mass Index (BMI). This addition aims to enrich the dataset by providing a standardized indicator of an athlete's body composition, which is particularly relevant in the context of sports performance.

The SQL query I constructed calculates the BMI for each athlete within the database, ensuring that only records with non-null Height and Weight values are included. By dividing Weight in kilograms by the square of Height in meters, the BMI is computed as per standard definitions. The resulting BMI values are sorted in descending order, grouped by Sport, to facilitate a clear comparison of body compositions across different athletic disciplines. This calculated metric could serve as a critical variable for future analyses related to athletic performance, health, and selection for sports categories.
<p align="center">
  <img src="https://github.com/russian17/ML/assets/120457811/064552db-9f70-43ee-b4e4-3b394d6d07d7" />
</p>

In the report, I've presented a table that quantifies the distribution of medals across Olympic Games over time. The creation of ratios for gold, silver, and bronze medals against the total medals awarded gives us a clear, quantifiable measure to observe trends and proportions within the data.

The medal_ratio is consistently set to 1.0, which confirms that for every event captured in the dataset, medals were indeed awarded. The gold_ratio, silver_ratio, and bronze_ratio are particularly insightful, as they reveal the proportion of each medal type out of the total medals awarded. These ratios remain relatively stable across the years, suggesting a consistent awarding process in the Olympics, with each type of medal being distributed in a relatively fixed proportion.

This information is invaluable for understanding how medal distributions have remained constant or changed over time, providing insights into the historical context of the Olympics, the evolution of sports, and perhaps the impact of various geopolitical and global events on the games. It's a testament to the enduring structure of the Olympic Games and the fair and standardized distribution of honors among athletes.

<p align="center">
  <img src="https://github.com/russian17/ML/assets/120457811/5fb59c33-2196-4740-b0cd-66ad86100797" />
</p>

## Go Broader 

Incorporating BMI into our dataset offers a compelling perspective when analyzing the bar chart. It's evident that sports such as weightlifting have participants with notably higher BMIs, a likely reflection of the sport's emphasis on strength and muscle mass. At the opposite end, disciplines like rhythmic gymnastics showcase lower BMIs, indicative of the agility and lean physique favored in the sport. This chart underscores the diverse physical demands across various sports and affirms the relevance of BMI as a useful metric for examining athletes' physical characteristics in relation to their sport.

<p align="center">
  <img src="https://github.com/russian17/ML/assets/120457811/3c56c584-626f-4955-901d-fbd5060e3d4f" />
</p>

The graph titled "Evolution of Medals" that I've included in my report portrays the trends in medal ratio distribution over the years for the Olympic Games. Each line represents one of the medal types — gold, silver, and bronze — allowing us to observe their relative prevalence across different Olympic years.

What stands out from this visualization is the fluctuation in ratios, particularly in the earlier years, which could be attributed to a variety of historical events affecting the games, such as the world wars or the varying number of participating nations and events. However, as we move towards the present, the ratios of gold, silver, and bronze medals stabilize, demonstrating the standardization of the Olympic Games' format over time.

The shaded areas around each line suggest the variance or uncertainty in the medal ratios, which also appears to decrease over the years, pointing towards more consistent outcomes in Olympic events. This visualization is instrumental in highlighting how the distribution of Olympic honors has evolved and become more structured, offering a clear visual narrative of Olympic history from the perspective of medal awards.

<p align="center">
  <img src="https://github.com/russian17/ML/assets/120457811/b7b13908-7086-491d-94c7-4543adec5486" />
</p>

