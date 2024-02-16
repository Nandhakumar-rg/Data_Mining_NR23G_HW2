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
    level1["smoking_info_gain"] = 0.2781

    level1["cough"] = -1.
    level1["cough_info_gain"] = 0.0349

    level1["radon"] = -1.
    level1["radon_info_gain"] = 0.2365

    level1["weight_loss"] = -1.
    level1["weight_loss_info_gain"] = 0.029

    level2_left["smoking"] = -1.
    level2_left["smoking_info_gain"] = -1.
    level2_right["smoking"] = -1.
    level2_right["smoking_info_gain"] = -1.

    level2_left["radon"] = 1.
    level2_left["radon_info_gain"] = 0.7219

    level2_left["cough"] = -1.
    level2_left["cough_info_gain"] = 0.3219

    level2_left["weight_loss"] = -1.
    level2_left["weight_loss_info_gain"] = 0.171

    level2_right["radon"] = 1.
    level2_right["radon_info_gain"] = 0.7219

    level2_right["cough"] = -1.
    level2_right["cough_info_gain"] = 0.3219

    level2_right["weight_loss"] = -1.
    level2_right["weight_loss_info_gain"] = 0.171

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    # Fill up construct_tree`
    # tree, training_error = construct_tree()
    tree = u.BinaryTree("smoking == Yes")  # MUST STILL CREATE THE TREE ***
    A = tree.insert_left("cough = Yes")
    B = tree.insert_right("randon == Yes")
    A.insert_left("y")
    A.insert_left("y")
    A.insert_left("y")
    A.insert_left("y")
    A.insert_left("n")
    B.insert_left("y")
    B.insert_right("n")
    B.insert_right("n")
    B.insert_right("n")
    B.insert_right("n")
    # tree, training_error = construct_tree
    # tree = U.BinaryTree("root")
    answer["tree"] = tree  # use the Tree structure
    # answer["training_error"] = training_error
    answer["training_error"] = 0.0  

    return answer


# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.4253642047367425
    # Infogain
    answer["(b) x < 0.2"] = 0.17739286055515824
    answer["(b) x <= 0.7"] = 0.3557029418697566
    answer["(b) y <= 0.6"] = 0.34781842724338197

    # choose one of 'x=0.2', 'x=0.7', or 'x=0.6'
    answer["(c) attribute"] = "y=0.6"  

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("y <= 0.6")
    left = tree.insert_left("x <= 0.7")
    right = tree.insert_right("x <= 0.2")

    left.insert_left("B")
    
    y_03 = left.insert_right("y <= 0.3")
    y_03.insert_left("A")
    y_03.insert_right("C")

    right.insert_right("A")
    y_08 = right.insert_left("y <= 0.8")
    y_08.insert_right("B")
    y_08.insert_left("C")
    answer["(d) full decision tree"] = tree

    return answer


# ----------------------------------------------------------------------


def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5

    # float
    answer["(b) Gini, ID"] = 0.0
    answer["(c) Gini, Gender"] = 0.48
    answer["(d) Gini, Car type"] = 0.1625
    answer["(e) Gini, Shirt type"] = 0.4914405

    answer["(f) attr for splitting"] = "Car type"

    # Explanatory text string
    answer["(f) explain choice"] = "Car Type is chosen for splitting at the root node due to its expected higher potential to differentiate between classes based on the problem context, as different car types might correlate more strongly with the target classes compared to other attributes."

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    
    answer["a"] = ['Continuous', 'Quantitative', 'Ratio']
    answer["a: explain"] = "Continuous because each measure can be subdivided into smaller measures without end. Quantitative due to its numerical value significance. Ratio because there's a true zero; at midnight, marking a new day, establishing a unique reference point."

    
    answer["b"] = ['Discrete', 'Quantitative', 'Ratio']
    answer["b: explain"] = "Discrete since even the smallest measurement units are distinct. Quantitative for its numerical value. Ratio because of the true zero; absolute darkness signifies no return to light."

    
    answer["c"] = ['Discrete', 'Qualitative', 'Ordinal']
    answer["c: explain"] = "Discrete with limited descriptors for light levels. Qualitative as assessment is based on judgment. Ordinal as descriptions imply a sequence like 'Dim', 'Bright', to 'Very Bright'."

    
    answer["d"] = ['Continuous', 'Quantitative', 'Ratio']
    answer["d: explain"] = "Continuous as measurements can be infinitely fine (e.g., 0.00000000000023°). Quantitative for its numerical nature. Ratio because of the non-negativity; angles can't be negative."

    
    answer["e"] = ['Discrete', 'Qualitative', 'Ordinal']
    answer["e: explain"] = "Discrete due to the three distinct levels. Qualitative as it's categorized by titles rather than numbers. Ordinal for denoting performance order."

    
    answer["f"] = ['Continuous', 'Quantitative', 'Interval']
    answer["f: explain"] = "Continuous as measures can be infinitely subdivided. Quantitative for its reliance on numerical value. Interval due to the absence of a true zero; analogous to temperature scales."

   
    answer["g"] = ['Discrete', 'Quantitative', 'Ratio']
    answer["g: explain"] = "Discrete as it counts in natural numbers. Quantitative due to numerical significance. Ratio because of the true zero; negative patients are impossible."

    
    answer["h"] = ['Discrete', 'Qualitative', 'Nominal']
    answer["h: explain"] = "Discrete since fractions of an ISBN don't exist. Qualitative as it serves as an identifier. Nominal for its exclusive use for identification without hierarchy."

    
    answer["i"] = ['Discrete', 'Qualitative', 'Ordinal']
    answer["i: explain"] = "Discrete with only three levels. Qualitative as it's based on judgment. Ordinal for ranking opacity to translucency."

    
    answer["j"] = ['Discrete', 'Qualitative', 'Ordinal']
    answer["j: explain"] = "Discrete with a fixed count of military ranks. Qualitative as it's based on rank, not number. Ordinal for the hierarchy it represents."

    
    answer["k"] = ['Continuous', 'Quantitative', 'Ratio']
    answer["k: explain"] = "Continuous with infinitely divisible measures. Quantitative for numerical importance. Ratio due to the true zero; being at the center defines a unique starting point."

    
    answer["l"] = ['Continuous', 'Quantitative', 'Ratio']
    answer["l: explain"] = "Continuous as density can vary infinitely. Quantitative for its numerical base. Ratio because zero density, though theoretical, establishes a baseline."

    
    answer["m"] = ['Discrete', 'Qualitative', 'Nominal']
    answer["m: explain"] = "Discrete as coat check numbers are indivisible. Qualitative for being identifiers. Nominal as they're used solely for identification, without implying order or quantity."

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
    answer["a, level 1"] = "x <= 0.5"
    answer["a, level 2, right"] ="A"
    answer["a, level 2, left"] = "y <= 0.4"
    answer["a, level 3, left"] = "A"
    answer["a, level 3, right"] = "x <= 0.2"

    # run each datum through the tree. Count the number of errors and divide by number of samples. .
    # Since we have areas: calculate the area that is misclassified (total area is unity)
    # float between 0 and 1
    answer["b, expected error"] = 0.58

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("x <= 0.5")

    A = tree.insert_right("A")
    B = tree.insert_left("y <= 0.4")
    B.insert_left("A")
    B.insert_right("x <= 0.2")
    answer["c, tree"] = tree
    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.5310044

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.23137821315975915
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

