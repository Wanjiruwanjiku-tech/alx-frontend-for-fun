# Syntatical AWSOME Stylesheets (Sass).

- Sass is a css preprocessor scripting language that is interpreted or compiled into Cascading Style Sheets.

-  It allows you to use 
1. Variables
2. Nested rules
3. Mixins
4. Functions etc
with a css compatible syntax.

## Writing Sass and SCSS

- Sass files have two syntax options
1. .sass
2. .scss

- .sass uses indentation to seperate code blocks while .scss uses curly braces like in CSS. 

### simple example of saas syntax

        $primary color: #333

        body
            font : 100% Helvetica, san-serif
            color: $primary-color

### Equivalent example to scss syntax

      $primary-color : #333;

      body {
        font : 100% Helvetica, san-serif
        color: $primary-color
      }


## Differrence between Sass and SCSS
- The main difference between the two is that .sass uses indentation while .scss uses brsces and semicolond to seperate code blocks.

# Tasks
0. In sass you can print something directly to the console
example

$debug-mode: true;

    @if $debug-mode {
      // Print debug message
      @debug "This is a debug message!";
    }

    // Rest of your Sass code...

The __@debug__ directive is used to print a message to the debug console