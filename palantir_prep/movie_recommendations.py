# Movie Recommendation System
#
# There are n users. Each user likes a range of movies, given by the segment [l_i, r_i] (inclusive).
# A user j is a predictor for user i (where j != i) if the range [l_j, r_j] fully contains [l_i, r_i] and [l_j, r_j] ≠ [l_i, r_i].
# A movie is strongly recommended to user i if:
#   - The movie is not already liked by user i (i.e., not in [l_i, r_i]), and
#   - The movie is liked by every predictor of user i (i.e., in the intersection of all predictors' ranges).
# For each user, compute the number of strongly recommended movies.
# If a user has no predictors, output 0 for that user.
#
# Input:
#   n (number of users)
#   n lines, each with two integers l_i and r_i
#
# Output:
#   n integers: the i-th is the number of strongly recommended movies for user i.
#
# Example:
# Input:
#   3
#   3 8
#   2 5
#   4 5
#
# Output:
#   0 0 1
#
# Implement the function below:

def strongly_recommended_movies(users):

    lines = users.strip().split('\n')
    num_users = int(lines[0])
    movie_users = []

    for i in range(num_users):
        l_str, r_str = lines[i + 1].split()
        l = int(l_str)
        r = int(r_str)
        movie_users.append((l, r))

    num_strong_recommendations = [0] * num_users

    def get_predictors(l, r):
        predictors = []
        for i in range(num_users):
            if movie_users[i] != (l, r):
                potential_predictor = movie_users[i]
                if potential_predictor[0] <= l and r <= potential_predictor[1]:
                    predictors.append(potential_predictor)
        return predictors

    def merge_predictors(predictors):
        if not predictors:
            return []
        
        result = [predictors[0][0], predictors[0][1]]

        for predictor in predictors[1:]:
            result[0] = max(result[0], predictor[0])
            result[1] = min(result[1], predictor[1])
        
        return result if result[0] < result[1] else []

    def get_overlap(predictors, l, r):
        left_overlap = l - predictors[0]
        right_overlap = predictors[1] - r
        return right_overlap + left_overlap


    for i in range(num_users):
        l, r = movie_users[i]

        predictors = get_predictors(l, r)

        predictors_merged = merge_predictors(predictors)

        if not predictors_merged:
            continue
            
        num_strong_recommendations[i] = get_overlap(predictors_merged, l, r)

    return num_strong_recommendations

test_input = """3
3 8
2 5
4 5"""

print(strongly_recommended_movies(test_input))
