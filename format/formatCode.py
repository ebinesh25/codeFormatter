import subprocess
import tempfile
import os

def format_code(code, language):
    """
    Formats the given code based on the programming language.

    :param code: The unformatted code as a string.
    :param language: The programming language (e.g., 'python', 'javascript').
    :return: The formatted code as a string or an error message.
    """
    formatters = {
        "python": "black",  
        "javascript": "prettier",  
        "html": "prettier", 
        "css": "prettier", 
        "json": "prettier",
        "c": "clang-format",
        "cpp": "clang-format",
        "java": "clang-format",
        "php": "php-cs-fixer",
        "sql": "sql-formatter-cli"
    }

    if language not in formatters:
        return f"Error: No formatter available for language '{language}'"

    formatter = formatters[language]

    # Write code to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{language}") as temp_file:
        temp_file.write(code.encode())
        temp_file_path = temp_file.name
        
    try:
        # Run the formatter as a subprocess
        if formatter == "black":
            subprocess.run([formatter, temp_file_path], check=True)
        elif formatter == "prettier":
            subprocess.run([formatter, "--write", temp_file_path], check=True)
        elif formatter == "clang-format":
            subprocess.run([formatter, temp_file_path], check=True)
        elif formatter == "php-cs-fixer":
            subprocess.run([formatter, "fix", temp_file_path], check=True)
        elif formatter == "sql-formatter-cli":
            subprocess.run([formatter, temp_file_path, "--output", temp_file_path], check=True)

        # Read the formatted code
        with open(temp_file_path, "r") as formatted_file:
            formatted_code = formatted_file.read()

        return formatted_code

    except subprocess.CalledProcessError as e:
        return f"Error: Failed to format code. {str(e)}"

    finally:
        # Clean up the temporary file
        os.remove(temp_file_path)

# Example usage
if __name__ == "__main__":
    unformatted_code = '''
    <?php
    function ajax_generate_nav_items($parentTitle = '') {$key = $_POST['key'];$parentIndex = $_POST['parentKey'] ?? -1;$level = $_POST['level'] ?? 0;$html = '';$items = get_new_nav_bar_data();if( $level == 1) {echo generate_nav_items();} else {if ( $parentIndex == -1 ) {$parentIndex = $key;$items= $items[$key];$parentTitle = $items['title'];$contents = $items['content'];$level = 1;} else {$items = $items[$parentIndex];$parentTitle = $items['content'][$key]['title'];$contents = $items['content'][$key]['subContent'];$level = 2;}$html = "<div class=' sidebar-items-list sidebar-submenu'".($parentIndex ? " data-parent-index='$parentIndex'" : "") . ">";if ( $parentIndex != -1 ) {$html .= "<div class='sidebar-item submenu-back-button' key=$parentIndex data-level=$level>";$chevron_right_icon = file_get_contents(get_template_directory() . '/assets/images/icons/svgs/chevron-right-white.svg');$html .= "<span style='transform: rotate(180deg)'>$chevron_right_icon</span>";$html .= "<span class='link-label'>$parentTitle</span>";$html .= "</div>";}foreach ($contents as $index => $item) {$title = $item['topicTitle'] ?? $item['topicShortTitle'] ?? $item['title'] ?? 'poda';$url = $item['path'] ?? '#';$hasContent = isset($item['content']) || isset($item['subContent']);$keyAttribute = " key='$index'";$dataAttribute = " data-parent-index=$parentIndex";if ($hasContent) {$html .= "<div class='sidebar-item' $keyAttribute $dataAttribute>";$chevron_right_icon = file_get_contents(get_template_directory() . '/assets/images/icons/svgs/chevron-right-white.svg');$html .= "<span class='link-label'>$title</span>$chevron_right_icon";$html .= "</div>";} else {$html .= "<div class='topic-link'><a href=/$url class='sidebar-item'$keyAttribute>";$html .= $title;$html .= "</a></div>";}}$html .= "</div>";echo $html;}wp_die();
}
    
    '''
    language = "php"
    formatted_code = format_code(unformatted_code, language)
    print("Formatted Code:\n", formatted_code)      
