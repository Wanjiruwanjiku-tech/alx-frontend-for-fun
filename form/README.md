# FORMS

## CREATING AN HTML5 FORM

- Creating a form in html5 strts with the __<form></form>__ tags.
- Here is a basic example

        <form action="/submit_form" method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            
            <input type="submit" value="Submit">
        </form>

1. Form Tag.

- The tag is used to create an html form
- The __action__ attr specifies the url where the data will be submitted to
- The __method__ attr specifies the HTTP method to be used when submitting the form. In this case 'post' is used, this means that the form data will be sent as a POST req.

2. Label Tag.

- Defines a label for an input element. it improves accessibility by associating the label with its corresponding input field.
- The __for__ attr specifies which inpu element the label is for. it should match the 'id' of the input element.

3. Input Tag.

- The input element creates a filed where a user can enter details.
- The __type__ attr specifies the type of input field. Examples include 'text', 'email', 'checkbox' e.t.c.
- The __id__ attr uniquely identifies the input element. It should __MATCH THE __FOR__ ATTR OF THE CORRESPONDING LABEL.__
- The __name__ attr specifies the name of the input field which is used when submitting the form data to the server.
- The __required__ attr is a boolean attr that indicates the input must be filled before submitting.

4. <input type="submit">
- This creates a submit button within the form. The __value__ attr specifies the text displayed on the button.

## CHOOSING THE RIGHT INPUT TYPE

- HTML5 provides various input types to improve form validation and user experience. Some common types include:-
1. text
2. email
3. password
4. number
5. date
6. checkbox
7. radio, etc.

- Choose the appropriate type based on the data you want to collect and the validation you need.

## CONSTRAINING A FORM WITH REGULAR EXPRESSIONS.

- You can use the pattern attribute along with a regular expression to constrain the input value.

- For example, to validate a phone number:

        <input type="text" id="phone" name="phone" pattern="[0-9]{10}" required>


## STYLING INPUTS FOR INVALID, VALID AND REQUIRED FIELDS

- You can use CSS pseudo-classes to style inputs based on their validation state.

- They include:

1. :valid
2. :invalid
3. :required

        ```CSS
        input:invalid {
            border-color: red;
        }

        input:valid {
            border-color: green;
        }

        input:required {
            background-color: yellow;
        }


## BUILDING A COMMENT FORM

- A comment form typically includes a text area for the comment content and maybe some other fields like name and email for identification

        <form action="/submit_comment" method="post">
            <label for="comment">Comment:</label>
            <textarea id="comment" name="comment" required></textarea>
            
            <label for="name">Name:</label>
            <input type="text" id="name" name="name">
            
            <input type="submit" value="Submit">
        </form>


## BUILDING A SIMPLE SEARCH FORM

- A search form typically includes a text input for entering the search query and a submit button.

- Here's a basic example:

            <form action="/search" method="get">
                <input type="text" name="query" placeholder="Search..." required>
                <input type="submit" value="Search">
            </form>



## CREATING USABLE AND ACCESSIBLE FORMS

* Use appropriate labels (<label>) for each form control to improve accessibility.

* Provide clear instructions and error messages.

* Ensure sufficient color contrast for visually impaired users.

* Use semantic HTML elements.

* Test your forms with keyboard-only navigation to ensure they are usable without a mouse.