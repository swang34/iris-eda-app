import streamlit as st 

def main():
	"""A simple EDA App"""
	st.title("Iris EDA APP with Streamlit")
	st.subheader("ST app test")

	activity = ["eda","prediction","countries","metrics","about"]
	choice = st.sidebar.selectbox("Choose Activity",activity)

	if activity == 'eda':
		st.subheader("EDA")
if __name__ == '__main__':
	main()