# CS-340-10523-M01-Client-Server-Development
CS 340 – Module Eight Journal Reflection
How do you write programs that are maintainable, readable, and adaptable?

To write maintainable and readable programs, I focus on modular design, clear structure, and separation of concerns. In Project One, I developed a reusable CRUD Python module that handled all database operations independently from the dashboard interface. This approach improved maintainability because database logic was isolated from user interface logic, making debugging and updates easier. If changes were required in the database structure, they could be implemented within the CRUD module without rewriting the dashboard code.

Working this way also improved adaptability. The CRUD module can be reused in future projects that require MongoDB connectivity. For example, I could integrate it into another analytics dashboard, an API backend, or a reporting system. By designing reusable components, I reduce duplication and increase scalability for future applications.

How do you approach a problem as a computer scientist?

When approaching the Grazioso Salvare dashboard project, I first analyzed the client’s requirements and translated them into technical specifications. I identified the data fields needed for filtering, visualization, and mapping. Then, I designed the database queries before building the user interface components.

This project differed from earlier assignments because it required integrating multiple technologies: MongoDB, Python, Dash, and data visualization tools. Instead of solving isolated coding problems, I built a complete system that connected the database to interactive visual components.

In the future, I would continue to:
- Break large problems into smaller modules
- Design database schemas before implementation
- Build reusable data access layers
- Test queries independently before integrating them into applications
This structured approach ensures systems are scalable and client-focused.

What do computer scientists do, and why does it matter?

Computer scientists design systems that transform raw data into meaningful information. In this project, the dashboard helped Grazioso Salvare quickly identify animals that meet rescue training criteria. Instead of manually reviewing thousands of records, the organization can filter, visualize, and analyze data efficiently.

Projects like this improve decision-making, reduce human error, and save time. By building reliable data systems, computer scientists enable organizations to operate more effectively and make evidence-based decisions.

For a company like Grazioso Salvare, this means:
- Faster identification of suitable rescue animals
- Better resource allocation
- Improved operational efficiency

Data-driven planning

This demonstrates how technical solutions directly support real-world impact.
