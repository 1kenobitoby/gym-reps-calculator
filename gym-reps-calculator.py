import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression


st.set_page_config(
    page_title="Weight training repetitions calculator",
    page_icon="media/favicon.ico",
    layout="centered",
    initial_sidebar_state="auto",
    #menu_items={
        #'Get Help': '<<URL>>',
        #'Report a bug': "<<URL>>",
        #'About': "Made with Streamlit v1.27"
    #}
)

# html strings used to render donate button and link and text
donate_text = '<h6> Useful? Buy us a coffee. </h6>'

html_donate_button = '''
<form action="https://www.paypal.com/donate" method="post" target="_blank">
<input type="hidden" name="hosted_button_id" value="6X8E9CL75SRC2" />
<input type="image" src="https://www.paypalobjects.com/en_GB/i/btn/btn_donate_SM.gif" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button"/>
<img alt="" border="0" src="https://www.paypal.com/en_GB/i/scr/pixel.gif" width="1" height="1" />
</form>
'''   

def redirect_button(url: str):
    st.markdown(
    f"""
    <a href="{url}" target="_blank">
        <div>
        <img src="https://www.paypalobjects.com/en_GB/i/btn/btn_donate_SM.gif" alt="Donate with PayPal button">
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )   

st.image('media/logo.png', width=100)
st.title('Weight training repetitions calculator')

st.write('When weight training, most people are familiar with the idea that as you add more weight to the bar, the number of repetitions you can do goes down. If a training programme calls for 12 repetitions of an exercise, how much weight should you put on the bar? This app calculates this for you by reference to your \'*1 rep max (1RM)*\', the amount of weight that is so high you could only perform one repetition of the exercise *with good form* before failure.')
st.write('You can use the app in one of two ways: either work out what your 1RM for an exercise is and then the app suggests rep targets for the same exercise using lower weights; or pick a lower weight and count how many reps you can do to failure and use that as an input to estimate your 1RM')

units = st.radio('Select your weight units', ('lbs', 'kg'))

column1, column2 = st.columns([0.5, 0.5])
with column1:
    weight = st.number_input('What weight were you lifting?', min_value=0.0, max_value=1000.0, step=0.5, value=None, format="%.1f")
with column2:
    reps = st.number_input('And how many reps did you manage with good form?', min_value=0, max_value=20, step=1, value=None)

# linear regression parameters of standard percentage of percentage of RM (y) plotted against number of reps (x)
m = -2.571
c = 100.71

if reps != None and weight != None:
    if reps == 1:
        calc1rm = weight
    else:
        calc1rm = weight/((reps*m+c)/100)

    # Make a list of reps with from zero to 20
    reps=[]
    for i in range(21):
        reps.append(i)
    # And loop percentages into it from regression equation
    percentages = []
    for i in reps:
        percentages.append(m*i+c)
    percentages[1] = 100
    weights = []
    for percent in percentages:
        weights.append(calc1rm*(percent/100))

    st.write('\n') 
    st.markdown('<strong><em><span style="color:#F63366;">Based on your inputs, here\'s your table of suggested weights and reps:</span></em></strong>', unsafe_allow_html=True)  
    
    weight_col, pc_col, rep_col = st.columns([0.33, 0.33, 0.33])

    with weight_col:
        st.write('***Weight, ' + units + '***')
        for j in range(1, 21, 1):
            st.write("%.1f" % weights[j])

    with pc_col:
        st.write('***% of 1RM***')
        for k in range(1, 21,1):
            st.write("%.0f" % percentages[k])

    with rep_col:
        st.write('***Reps***')
        for l in range(1, 21,1):
            st.write("%.0f" % reps[l])

st.write('\n')
st.markdown('<strong><em>For maximum <span style="color:#F63366;">strength</span> gains, do <span style="color:#F63366;">sets of 3 to 6 reps</span>, performing the exercises slowly, not going to failure and taking several minutes rest between sets</em></strong>', unsafe_allow_html=True)
st.markdown('<strong><em>For maximum <span style="color:#F63366;">power</span> gains (force multiplied by speed), do <span style="color:#F63366;">sets of about 6 reps</span>, performing the concentric (contraction) phase as quickly as you can while maintaining good form</em></strong>', unsafe_allow_html=True) 
st.markdown('<strong><em>For <span style="color:#F63366;">hypertrophy</span> (growing big muscles), do <span style="color:#F63366;">sets of between 8 and 12 reps</span>, performing the exercises slowly with a minute or two between sets and taking the last set to failure</em></strong>', unsafe_allow_html=True) 
st.markdown('<strong><em>To develop  <span style="color:#F63366;">muscular endurance</span>  and strong connective tissues do <span style="color:#F63366;">sets of 15 to 20 reps</span></em></strong>', unsafe_allow_html=True)           

st.write('\n')
st.write('\n')
donate_left, donate_right = st.columns([1, 3])
with donate_left:
    st.write('\n')
    st.markdown(donate_text, unsafe_allow_html=True)

with donate_right:
    st.write('\n')
    redirect_button("https://www.paypal.com/donate/?hosted_button_id=6X8E9CL75SRC2")    

st.divider()
st.write('*Need to tweak the table a bit? Expand the Notes section to find out how.*')

st.write('\n')
with st.expander("Notes"):
    st.markdown('The standard table above is about right for the majority of people. If you are a long, skinny type (what is known as an *ectomorph*) you might find that you can do the high rep sets fine but the weights are too much for the lower rep range end of the table. Conversely, if you have a squat, chunky frame (an *endomorph*) you might find you can manage the weight suggested in the low rep ranges but can\'t complete the sets with the suggested weights in the 15 to 20 rep ranges. If either of those sounds like your experience, you can tweak the table to suit your physiology.<br><br>Pick an exercise and choose a heavy weight so you can only manage a few reps to failure. Note the weight and number of reps. Have a rest and do the same exercise with a lighter weight that you can manage somewhere between 12 and 20 reps with. Again, note the weight and number of reps. Enter them below. Using the power of magic a new table of weights and reps more appropriate to you for this exercise will appear below.', unsafe_allow_html=True)
    set1_col, set2_col = st.columns([0.5, 0.5])
    with set1_col:
        set1w = st.number_input('What weight were you lifting on set 1?', min_value=0.0, max_value=1000.0, step=0.5, value=None, format="%.1f", key='set1w')
        st.write('\n')
        st.write('\n')
        set2w = st.number_input('What weight were you lifting on set 2?', min_value=0.0, max_value=1000.0, step=0.5, value=None, format="%.1f", key='set2w')
    with set2_col:
        set1r = st.number_input('And how many quality reps did you manage on set 1?', min_value=0, max_value=20, step=1, value=None, key='set1r')
        st.write('\n')
        st.write('\n')
        set2r = st.number_input('And how many quality reps did you manage on set 2?', min_value=0, max_value=20, step=1, value=None, key='set2r')
    if set1w and set2w and set1r and set2r:
        if set1w <= set2w and set1r <= set2r or set1w >= set2w and set1r >= set2r:
            st.write('***That doesn\'t make sense. Your heavier weight set should have fewer reps than your lighter weight set. Please go back and check your inputs.***')
        else:
            st.write('\n')
            # https://realpython.com/linear-regression-in-python/
            # Put the rep data into a 2D array with n rows and 1 column
            x = np.array([set1r, set2r]).reshape((-1,1))
            # Put the weight data into a 1D array with n rows
            y = np.array([set1w, set2w])
            # Create an instance of class LinearRegression using 'model' as the variable name and call 'fit' on it to calculate the regression parameters
            model = LinearRegression().fit(x, y)
            # Note this is a graph of weight (y) against number of reps (x) so it's a diffrent model to the first example (which is % of rm (y) against number of reps)
            # Model parameters. Rsquared should always be 1 as there are only two data points
            # r2 = model.score(x, y)
            intercept = model.intercept_
            gradient = model.coef_

            # Make a list of reps with from zero to 20
            tweak_reps=[]
            for i in range(21):
                tweak_reps.append(i)

            # And loop weights into it from regression equation
            tweak_weights = []
            for rep in tweak_reps:
                tweak_weights.append(rep*gradient+intercept)
 
            # Now work out the percentages by dividing the current weight by 1RM (tweak_weight[1])
            tweak_percentages = []
            for weight in tweak_weights:
                tweak_percentages.append(100*weight/tweak_weights[1])

               
            st.write('\n')
            st.markdown('<strong><em><span style="color:#F63366;">Here\'s your tweaked table of suggested weights and reps:</span></em></strong>', unsafe_allow_html=True)  
            
            t_weight_col, t_pc_col, t_rep_col = st.columns([0.33, 0.33, 0.33])

            with t_weight_col:
                st.write('***Weight, ' + units + '***')
                for j in range(1, 21, 1):
                    st.write("%.1f" % tweak_weights[j])

            with t_pc_col:
                st.write('***% of 1RM***')
                for k in range(1, 21,1):
                    st.write("%.0f" % tweak_percentages[k])

            with t_rep_col:
                st.write('***Reps***')
                for l in range(1, 21,1):
                    st.write("%.0f" % tweak_reps[l])
                    
            st.write('\n')
            st.markdown('This works by performing a linear fit to your two input sets so the further apart they are in terms of weight and number of reps the better. If you get nonsense results try and use a more widely spaced pair of sets. Or just go back to the standard table above. And in all cases, don\'t forget to include the weight of the bar when inputting your weights (for olympic bars it could be as much as 20kg).', unsafe_allow_html=True)

    st.write('\n')
    st.markdown('<small>*Comments, queries or suggestions? [Contact us](https://www.elephant-stone.com/contact.html)*.</small>', unsafe_allow_html=True)    


