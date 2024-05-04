import streamlit as st
import datetime
current_year = datetime.date.today().year

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image(
        "https://cdn.gencraft.com/prod/user/fd13fdb8-1200-4efe-a0ce-74e4bfdb0f4f/fdc57183-e538-49e7-abac-862d0dcc0712"
        "/image/image1_0.jpg?Expires=1714889074&Signature=fzRwYIBlN8XhAbut~H50Z6BFTleEwrFWE"
        "-KC545Y3VpUijBmjdL8lDQjAJufLDUWCUe9fnY7joIXEgqIFU9E3exTTQn2G4WVF81Nx~DuoRtjp1"
        "~vKGklJp1ThQuOzkOIoWXr8KewA1lFByPo4bAKWTsP"
        "-0DVy8dWYdEwmuvhFfJ6oNJnxHnC50vqYMYFTW9ESfhFLoL579wiEreitc6kOykK0iPYa8VPKthGzsfhgusaP3xCf8DuBSRC8Ge10YJpwFDhPbim5pzS~eQcRRfjHFZVzs6FADcK-qY4x2gKSu-JvbsUNm24wJ65wH1U5QLy07lwULx4xv3JUAUEy5~QiQ__&Key-Pair-Id=K3RDDB1TZ8BHT8")
with col2:
    st.title("Chiluru Santhosh Kumar Raju")
    content = """I am Santhosh, a passionate individual deeply immersed in the realms of programming and technology. 
    Currently navigating the dual roles of a CS student and an IT professional, I find myself continually drawn into 
    the fascinating world of Python programming. For me, it's not just about writing code; it's about uncovering new 
    possibilities and pushing the boundaries of what's achievable. With an unquenchable thirst for knowledge, 
    I eagerly embrace emerging technologies, finding immense joy in the ever-evolving landscape of innovation. In 
    this fast-paced digital era, I thrive on the excitement of learning and adapting, ready to seize every 
    opportunity for growth and development."""

    #st.write(content)

    st.info(content)
st.subheader("Below you can find some of the apps I have built in Python.")
col3, col4 = st.columns(2)
with col3:
    st.title("1. To do App")
    st.info("A to-do app is a digital organizer for managing tasks, deadlines, and priorities efficiently. It "
            "streamlines daily planning, offering features like task categorization, reminders, and progress "
            "tracking. With its user-friendly interface, it helps individuals stay focused and productive in both "
            "personal and professional endeavors.")
    st.image("https://tichung.com/blog/2021/20200323_flask"
             "/feature_hu3e648f129a6d3d9f6c88c7dbd8276791_92781_1320x0_resize_box_3.png")

    st.title("2. Project ShowCase")
    st.info("A portfolio website showcases an individual's work, skills, and accomplishments to potential clients or "
            "employers. It serves as a digital resume, offering a professional online presence to highlight expertise "
            "and attract opportunities.")
    st.image("https://i.pinimg.com/736x/14/3d/38/143d386b3df0507c1922814af4897e2f.jpg")

    st.title("3. Task Automation")
    st.info("Task automation involves using software or tools to streamline repetitive tasks, saving time and "
            "reducing human error by automating processes. By automating routine activities, businesses and "
            "individuals can increase efficiency and focus on more strategic and high-value work.")
    st.image("https://cdn.activestate.com/wp-content/uploads/2020/06/AutomatableTasks.jpg")

    st.title("4. Extracting Excel data and creating reports")
    st.info("Automating Excel data extraction involves using scripts or tools to gather information from "
            "spreadsheets, while report generation automates the process of compiling and formatting data into "
            "comprehensive reports, streamlining analysis and decision-making processes.")
    st.image("https://www.finereport.com/en/wp-content/uploads/2019/12/02.png")

    st.title("5. Automated daily news digest Emails with Python")
    st.info("Create a Python script that fetches relevant news articles from sources using APIs or web scraping, "
            "then formats and sends them via email to subscribers, providing a personalized daily news digest "
            "effortlessly.")
    st.image("https://cdn-rdstaticassets.readdle.com/spark/content_pages/templates_how-to-email-company/email-company"
             "-template.png")

    st.title("6. Build an API serving historical weather data")
    st.info("Develop a RESTful API using Python and a web framework like Flask or Django that queries a weather "
            "database based on location and date parameters, returning historical weather data in JSON format for "
            "integration into various applications and analysis purposes.")
    st.image("https://i.ytimg.com/vi/9P5MY_2i7K8/maxresdefault.jpg")

    st.title("7. Weather forecast data dashboard")
    st.info("Build a web-based dashboard using HTML, CSS, and JavaScript that fetches weather forecast data from a "
            "reliable API and displays it dynamically, offering users an intuitive interface to visualize upcoming "
            "weather conditions with interactive features for enhanced user experience.")
    st.image("https://miro.medium.com/v2/resize:fit:2000/1*XwC1OKFFjMQG7xD0fbrEIw.png")

    st.title("8. NLP of Ebooks")
    st.info("Leverage Natural Language Processing (NLP) techniques and libraries like NLTK or spaCy to analyze and "
            "extract insights from ebooks, enabling tasks such as sentiment analysis, keyword extraction, "
            "and topic modeling for deeper understanding and content summarization.")
    st.image("https://media.licdn.com/dms/image/D5612AQGMXZl6lgEwuA/article-cover_image-shrink_720_1280/0"
             "/1704547996941?e=2147483647&v=beta&t=bNTb7xBW50pxqHUQvTPOVwcwvhq4b2qnM2ulXKc-4aU")

    st.title("9. Webcam monitoring email alert app")
    st.info("Develop a Python application using OpenCV to monitor a webcam feed for predefined events or changes, "
            "triggering email alerts with relevant snapshots or notifications to designated recipients, "
            "enhancing security and surveillance measures with real-time monitoring capabilities.")
    st.image("https://store-images.s-microsoft.com/image/apps.51160.14274610339273393.3480a5e3-838b-4f58-97cc"
             "-f304bfbdab66.beb6adb2-3f63-455c-b20c-31c2e1dde2b9")

    st.title("10. Webscraping website")
    st.info("Utilize Python libraries like BeautifulSoup or Scrapy to programmatically extract desired data from web "
            "pages by parsing HTML structures, enabling efficient web scraping operations for various purposes such "
            "as data collection, market research, or content aggregation.")
    st.image("https://blog.apify.com/content/images/2023/09/what-is-web-scraping-websites-web-scraper-structured-data"
             "-1.png")

with col4:
    st.title("11. Hotel booking app")
    st.info("Create a mobile application with user-friendly interfaces and secure payment integration, allowing users "
            "to search for hotels based on preferences and book accommodations seamlessly, enhancing convenience and "
            "travel planning experiences.")
    st.image("https://cdn.dribbble.com/userupload/3486527/file/original-ed987c56b051ab939ecab3223519f57c.jpg?resize"
             "=2048x1536")

    st.title("12. Understanding the others code")
    st.info("Reviewing and comprehending others' code involves analyzing its structure, logic, and documentation, "
            "while experimenting with it and seeking clarification when necessary, fostering collaboration and "
            "knowledge-sharing within the development team.")
    st.image("https://miro.medium.com/v2/resize:fit:1400/1*kld8RKRjrouhdp4gWNFmBQ.jpeg")

    st.title("13. Student management system SQLite")
    st.info("Develop a student management system using SQLite as the database backend, allowing for efficient storage "
            "and retrieval of student information, grades, and attendance records, facilitating seamless "
            "administrative tasks and academic tracking within educational institutions.")
    st.image("https://repository-images.githubusercontent.com/475433661/07dc583f-c31b-4f2e-9b11-1db55c4bb2f9")

    st.title("14. Student management system MySQL")
    st.info("Design a student management system utilizing MySQL as the relational database management system, "
            "enabling robust data storage, querying, and management functionalities to handle student records, "
            "course details, grades, and administrative tasks efficiently within educational institutions.")
    st.image("https://www.sourcecodester.com/sites/default/files/images/Ronald%20Ronnie/dasboard.png")
    st.title("15. Intelligent Chatbot")
    st.info("Build an intelligent chatbot using machine learning models like LSTM or transformer architectures "
            "trained on vast datasets, implementing natural language processing techniques to understand and generate "
            "human-like responses, enhancing user engagement and providing personalized assistance across various "
            "domains and platforms.")
    st.image("data:image/jpeg;base64,"
             "/9j/4AAQSkZJRgABAQAAAQABAAD"
             "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")

    st.title("16. Job application web app with Flask")
    st.info("Create a job application web app using Flask, integrating user authentication, job listing, "
            "and application submission features, providing a seamless platform for job seekers and employers to "
            "connect and manage the recruitment process efficiently.")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTHQQkxEkhTeFAQjVqglU4CGdhg8QXfrJ_zg&usqp=CAU")

    st.title("17. Job application web app with Django")
    st.info("Develop a job application web app using Django, incorporating user authentication, job listing, "
            "and application submission functionalities, offering a robust and scalable platform for job seekers and "
            "employers to interact and manage the hiring process effectively.")
    st.image("https://i.pinimg.com/736x/30/d0/a4/30d0a49f371e5c00daaa7d61007a8e18.jpg")

    st.title("18. Restaurant Kitchen App")
    st.info("Design a restaurant kitchen app with a user-friendly interface and real-time order management, "
            "optimizing kitchen workflows and communication between chefs and staff for efficient food preparation "
            "and service, enhancing overall restaurant operations and customer satisfaction.")
    st.image("https://s3.envato.com/files/293134370/pos%20web%202.png")

    st.title("19. Movie Recommendation system")
    st.info("Implement a movie recommendation system using collaborative filtering techniques or machine learning "
            "algorithms like matrix factorization, analyzing user preferences and historical data to suggest "
            "personalized movie recommendations, enhancing user experience and engagement on streaming platforms.")
    st.image("https://cdn-images-1.medium.com/max/1500/1*leuI7fVkeOrKAIGOOj_T9A.png")

    st.title("20. Build and publish python  package")
    st.info("Create a Python package using setuptools or Poetry, including necessary modules and metadata, "
            "then publish it to the Python Package Index (PyPI) using the 'twine' package, enabling easy installation "
            "and distribution of your library for others to use.")
    st.image("https://www.pyopensci.org/python-package-guide/_images/publish-python-package-pypi-conda.png")

footer_html = """
<div style='text-align: center;'>
  <p>&copy; {year} CHILURU SANTHOSH KUMAR RAJU. All rights reserved. Developed with ❤️ using Streamlit</p>
</div>
""".format(year=current_year)
#st.set_page_config(page_title="Santhosh Portfolio", page_icon=":heart:")
st.markdown(footer_html, unsafe_allow_html=True)
st.image("https://media.istockphoto.com/id/1172175361/vector/thank-you-vector-typography-banner.jpg?s=612x612&w=0&k"
         "=20&c=j89bHclTv7MozKD1nxOP1HDvhEkL5BUp5VNcfCY-6xw=", width=1000)
