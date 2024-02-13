# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u


# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.
    level1["smoking_info_gain"] = 0.278

    level1["cough"] = -1
    level1["cough_info_gain"] = -1

    level1["radon"] = -1
    level1["radon_info_gain"] = -1

    level1["weight_loss"] = -1
    level1["weight_loss_info_gain"] = -1

    level2_left["smoking"] = -1
    level2_left["smoking_info_gain"] = -1
    level2_right["smoking"] = -1
    level2_right["smoking_info_gain"] = -1

    level2_left["radon"] = -1
    level2_left["radon_info_gain"] = -1

    level2_left["cough"] = 1
    level2_left["cough_info_gain"] = 0.722

    level2_left["weight_loss"] = -1
    level2_left["weight_loss_info_gain"] = -1

    level2_right["radon"] = 1
    level2_right["radon_info_gain"] = 0.722

    level2_right["cough"] = -1
    level2_right["cough_info_gain"] = -1

    level2_right["weight_loss"] = -1
    level2_right["weight_loss_info_gain"] = -1

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up `construct_tree``
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("root")  # MUST STILL CREATE THE TREE *****
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 0.
    # Infogain
    answer["(b) x <= 0.2"] = 0.
    answer["(b) x <= 0.7"] = 0.
    answer["(b) y <= 0.6"] = 0.

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = ""  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("Root")
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.
    answer["(d) Gini, Car type"] = 0.
    answer["(e) Gini, Shirt type"] = 0.

    answer["(f) attr for splitting"] = ""

    # Explanatory text string
    answer["(f) explain choice"] = ""

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal', 'quantitative', 'interval', 'ratio']
    answer["a"] = ["binary", "qualitative", "nominal"]
    answer["a: explain"] = "AM or PM offers only two options without a quantitative value, representing nominal data."

    answer["b"] = ["continuous", "quantitative", "ratio"]
    answer["b: explain"] = "Brightness can vary continuously and has a true zero (complete darkness), making it ratio."

    answer["c"] = ["discrete", "qualitative", "ordinal"]
    answer["c: explain"] = "People's judgments categorize brightness into ordered groups without precise numerical values."

    answer["d"] = ["continuous", "quantitative", "interval"]
    answer["d: explain"] = "Angles can vary continuously and have meaningful intervals, but 0 degrees is arbitrary, not an absence of angle."

    answer["e"] = ["discrete", "qualitative", "ordinal"]
    answer["e: explain"] = "Medals represent ordered categories without quantitative measurement."

    answer["f"] = ["continuous", "quantitative", "ratio"]
    answer["f: explain"] = "Height can vary continuously with a true zero point, representing ratio data."

    answer["g"] = ["discrete", "quantitative", "ratio"]
    answer["g: explain"] = "The number of patients is countable with a true zero, making it ratio data."

    answer["h"] = ["discrete", "qualitative", "nominal"]
    answer["h: explain"] = "ISBN numbers are unique identifiers without a quantitative relationship, representing nominal data."

    answer["i"] = ["discrete", "qualitative", "ordinal"]
    answer["i: explain"] = "These categories have a natural order based on the ability to pass light, but are not quantitative."

    answer["j"] = ["discrete", "qualitative", "ordinal"]
    answer["j: explain"] = "Military ranks are ordered categorically without quantitative measurement."

    answer["k"] = ["continuous", "quantitative", "ratio"]
    answer["k: explain"] = "Distance can be measured continuously with a true zero, qualifying as ratio data."

    answer["l"] = ["continuous", "quantitative", "ratio"]
    answer["l: explain"] = "Density varies continuously, has a true zero, and measurements are directly comparable, making it ratio."

    answer["m"] = ["discrete", "qualitative", "nominal"]
    answer["m: explain"] = "Coat check numbers are unique identifiers without quantitative value or order, representing nominal data."

    return answer



# ----------------------------------------------------------------------


def question5():
    explain = {}

    explain["a"] = "Model 2"
    explain["a explain"] = "Model 2 is expected to perform better on unseen instances because it shows higher accuracy on the testing set, indicating better generalization compared to Model 1, which appears to overfit the training data."

    explain["b"] = "Model 2"
    explain["b explain"] = "Despite Model 1 having a slightly higher overall accuracy, Model 2's consistent performance and better generalization to unseen data make it a preferable choice for future unseen instances."

    explain["c similarity"] = "Both techniques aim to prevent overfitting by considering model complexity."
    explain["c similarity explain"] = "MDL and the pessimistic error estimate both seek to balance fitting the training data well while keeping the model simple to generalize well to new data."

    explain["c difference"] = "Approach to incorporating model complexity."
    explain["c difference explain"] = "MDL uses a formalism based on data compression, while the pessimistic error estimate adjusts the error rate based on the tree size and the number of correctly classified instances."

    return explain



# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = ""
    answer["a, level 2, right"] =""
    answer["a, level 2, left"] = ""
    answer["a, level 3, left"] = ""
    answer["a, level 3, right"] = ""

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("root note")

    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.53100

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.23137
    answer["e, gain ratio, Handedness"] = 0.53100

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)

