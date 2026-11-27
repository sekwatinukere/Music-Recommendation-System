library(tidyverse)

music <- read_csv("data/processed/cleaned_tracks.csv", show_col_types = FALSE)

numeric_data <- music %>%
  select(popularity, danceability, energy, loudness,
         speechiness, acousticness, instrumentalness,
         liveness, valence, tempo)

print(round(cor(numeric_data, use = "complete.obs"), 2))

ggplot(music, aes(x = energy, y = popularity)) +
  geom_point(alpha = 0.35) +
  geom_smooth(method = "lm") +
  labs(title = "Energy vs Track Popularity")

genre_summary <- music %>%
  group_by(genre) %>%
  summarise(
    tracks = n(),
    avg_popularity = mean(popularity, na.rm = TRUE),
    avg_energy = mean(energy, na.rm = TRUE),
    avg_danceability = mean(danceability, na.rm = TRUE)
  ) %>%
  arrange(desc(avg_popularity))

print(genre_summary)

model <- lm(
  popularity ~ energy + danceability + valence + tempo + acousticness,
  data = music
)

summary(model)
