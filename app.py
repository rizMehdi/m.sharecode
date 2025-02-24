import streamlit as st

def main():
    st.title("IRESHA Sharecode")
    st.header("Immigration/Residence Status Eligibility for Social Housing Assistance - Sharecode")
    
    st.write("This webapp can be used to generate a sharecode indicating that you fulfil the minimum immigration/residence status eligibility requirements for social-housing assistance.")
    
    st.subheader("For applicants")
    st.write("To create a sharecode, you will be asked a series of questions to check if you have the minimum eligibility for social-housing assistance.")
    st.write("There might be additional requirements based on where you live or where you want to apply for social housing.")
    
    if st.button("Check eligibility and create sharecode"):
        option = st.radio("Are you any of the following?", [
            "British Citizen",
            "Irish Citizen",
            "Commonwealth Citizen ❓",
            "Diplomat or their family member based in the UK",
            "None of the above"
        ], help="A Commonwealth citizen is a citizen of a Commonwealth of Nations member state. Check here if your country is a commonwealth member: https://thecommonwealth.org/our-member-countries")
        
        st.write(f"You selected: {option}")
    
if __name__ == "__main__":
    main()
