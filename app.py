import streamlit as st

st.title('Utility Split Calculator')

bill_total = (st.number_input('Enter the total bill', min_value = 1, value = 100))
st.write("")


st.write('Select the number of groups for this bill')
groups = st.slider('Groups', 1, 5)


total_units = 0
group_dict = {}
for i in range(1, groups + 1):
	group_count = st.number_input(f'How many people in group {i}?', 1, key = i)
	group_days = st.number_input(f'How many days for this group? ({i})', 10, key = i+1)
	st.text("----------")
	total_units += group_count * group_days
	group_dict[f'Group {i}'] = [group_count, group_days, group_count * group_days]

total_collected = 0
i = 1
for key, value in group_dict.items():
	amount = int((bill_total * group_dict[key][2] / total_units) / group_dict[key][0])
	group_total = group_dict[key][0] * amount
	total_collected += group_total

	st.write(f'The {group_dict[key][0]} person(s) in Group {i} owe(s) ${amount}.')
	i +=1

st.write(f'Total collected will be ${total_collected}, which is ${bill_total - total_collected} less than the bill total (${bill_total}).')





