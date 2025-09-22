<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Query Selector</title>
</head>
<body>

    <?php
    $items = [
        ['id' => 1, 'name' => 'John', 'age' => 25],
        ['id' => 2, 'name' => 'Jane', 'age' => 30],
        ['id' => 3, 'name' => 'Doe', 'age' => 35], 
        ['id' => 4, 'name' => 'Doe', 'age' => 40]
    ];
    ?>
    <div>
        <?php
        foreach ($items as $item) {
            echo '<input type="hidden" class="selected-item" data-id="' . $item['id'] . '" value="' . htmlspecialchars(json_encode($item)) . '">';
        }
        ?>
    </div>
</body>

<script>
    const items = document.querySelectorAll('.selected-item');
    const SESSION_KEY = 'item_names';

    data = [];

    items.forEach(item => {
        const itemData = JSON.parse(item.value);
        console.log(item.dataset.id, itemData.name, itemData.age);
        data.push({
            id: itemData.id,
            name: itemData.name,
            age: itemData.age,
        });
    });
    sessionStorage.setItem(`${SESSION_KEY}`, JSON.stringify(data));
</script>

</html>