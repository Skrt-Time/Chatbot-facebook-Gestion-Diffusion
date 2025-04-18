const form = document.getElementById('queryForm');
const executeButton = document.getElementById('executeBtn');
if (executeButton !== null) {
    executeButton.addEventListener('click', executeRequest);
}

const conditionInputs = document.getElementById('conditionInputs');
<<<<<<< HEAD
const selectedField = document.getElementById('fieldSelect');
if (selectedField !== null) {
    selectedField.addEventListener('change', changeInputHtml);
}

const previewSqlButton = document.getElementById('previewSqlBtn');
if (previewSqlButton !== null) {
    previewSqlButton.addEventListener('click', () => {
        const sqlCodeDisplay = document.getElementById('sqlCodeDisplay');
        const sqlCode = document.getElementById('sqlCode');
        if (sqlCode !== null) { sqlCode.textContent = generateSqlQuery(); }
        if (sqlCodeDisplay !== null) { sqlCodeDisplay.style.display = 'block'; }
    });
}

=======
>>>>>>> main
let sqlQuery;
document.addEventListener('DOMContentLoaded', checkInput);


<<<<<<< HEAD

function checkInput() {
    const inputs = document.querySelectorAll('#conditionInputs input');
    const allFilled = Array.from(inputs).every(input => input.value.trim() !== '');

    if (previewSqlButton === null) {
        return;
    }

    if (selectedField !== null && selectedField.value != null && allFilled) {
        toggleExecuteButton();
        previewSqlButton.style.opacity = 1;
        previewSqlButton.style.display = 'block';
        previewSqlButton.classList.remove('inactive');

    } else {
        toggleExecuteButton(false);
        previewSqlButton.style.opacity = 0;
        setTimeout(() => {
            previewSqlButton.style.display = 'none';
        }, 300);
        previewSqlButton.classList.add('inactive');

    }
}

function changeInputHtml() {
    if (conditionInputs === null) {
        return;
    }


    let inputHtml = '';
<<<<<<< HEAD
    if (selectedField === 'date') {
=======
    if (selectedField.value === 'date') {
>>>>>>> 50d68ed (Amelioration du code & Ajout de la requête fetch pour communiquer avec le fichier execute_query.php)
=======
document.getElementById('fieldSelect').addEventListener('change', function() {
    const selectedField = this.value;
    const conditionInputs = document.getElementById('conditionInputs');
    conditionInputs.innerHTML = '';

    let inputHtml = '';
    if (selectedField === 'date') {
>>>>>>> main
        inputHtml = `
            <label for="startDate">Date de début:</label>
            <input type="date" id="startDate" name="startDate" oninput="checkInput()" value="<?php echo $StartDate;?>">
            <label for="endDate">Date de fin:</label>
            <input type="date" id="endDate" name="endDate" oninput="checkInput()">
        `;
<<<<<<< HEAD
<<<<<<< HEAD
    } else if (selectedField != 'all') {
        inputHtml = `<input type="text" name="conditionValue" id="conditionValue" placeholder="Valeur de condition" oninput="checkInput()" value="<?php echo $ConditionValue;?>">`;
=======
    } else if (selectedField.value) {
=======
    } else if (selectedField != 'all') {
>>>>>>> main
        inputHtml = `<input type="text" name="conditionValue" id="conditionValue" placeholder="Valeur de condition" oninput="checkInput()">`;
>>>>>>> 50d68ed (Amelioration du code & Ajout de la requête fetch pour communiquer avec le fichier execute_query.php)
    }

    conditionInputs.innerHTML = inputHtml;
    checkInput();
<<<<<<< HEAD
<<<<<<< HEAD

    // Gérer l'affichage de sqlCodeDisplay en fonction de la sélection
    const sqlCodeDisplay = document.getElementById('sqlCodeDisplay');
    if (selectedField !== 'date') {
        sqlCodeDisplay.style.display = 'none';
    } else {
        sqlCodeDisplay.style.display = 'block';
    }
});


=======

    // Reinitialiser l'affichage de sqlCodeDisplay en fonction de la sélection
    const sqlCodeDisplay = document.getElementById('sqlCodeDisplay');
    sqlCodeDisplay.style.display = 'none';
    });
//Afficher la requete
>>>>>>> main
document.getElementById('previewSqlBtn').addEventListener('click', function() {
    const selectedField = document.getElementById('fieldSelect').value;
    console.log("Selected Field:", selectedField);
=======

}
>>>>>>> 50d68ed (Amelioration du code & Ajout de la requête fetch pour communiquer avec le fichier execute_query.php)

function generateSqlQuery() {
    if (selectedField === null) {
        return;
    }
    console.log("Selected Field:", selectedField.value);

<<<<<<< HEAD
    const sqlCodeDisplay = document.getElementById('sqlCodeDisplay');
    const sqlCode = document.getElementById('sqlCode');
    sqlCode.textContent = sqlQuery;
    sqlCodeDisplay.style.display = 'block';
});
document.getElementById('executeBtn').addEventListener('click', function() {
    const selectedField = document.getElementById('fieldSelect').value;
<<<<<<< HEAD
    let sqlQuery = generateSqlQuery(selectedField);
    
    // Exécuter la requête SQL
    // Remplacez cette partie par votre propre code pour exécuter la requête
    const results = executeQuery(sqlQuery); // Supposons que executeQuery est une fonction qui exécute la requête SQL

    // Afficher les résultats dans le tableau
    const resultTableBody = document.getElementById('resultTableBody');
    resultTableBody.innerHTML = ''; // Nettoyer le contenu précédent du tableau
    
    for (let i = 0; i < results.length; i++) {
        const row = document.createElement('tr');
        
        // Ajoutez des cellules de données pour chaque champ dans l'enregistrement
        for (const key in results[i]) {
            if (results[i].hasOwnProperty(key)) {
                const cell = document.createElement('td');
                cell.textContent = results[i][key];
                row.appendChild(cell);
            }
        }
        
        // Ajoutez la case à cocher et la classe "glow" (à adapter)
        const checkboxCell = document.createElement('td');
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = true; // Par défaut, coché
        checkbox.addEventListener('change', function() {
            if (this.checked) {
                row.classList.add('glow');
            } else {
                row.classList.remove('glow');
            }
        });
        checkboxCell.appendChild(checkbox);
        row.appendChild(checkboxCell);
        
        // Ajoutez la ligne au tableau
        resultTableBody.appendChild(row);
    }

    // Afficher le tableau
    document.getElementById('resultTable').style.display = 'block';
});



=======
    //console.log("Selected Field:", selectedField);

    sqlQuery = generateSqlQuery(selectedField);
});
>>>>>>> main




<<<<<<< HEAD
//probleme ici avec le return de cette fonction
function generateSqlQuery(selectedField) {
    //console.log("Selected Field:", selectedField);

    let sqlQuery = '';
=======
>>>>>>> 50d68ed (Amelioration du code & Ajout de la requête fetch pour communiquer avec le fichier execute_query.php)
    const tableName = 'facebook_infos.users';
    const dateField = 'date';

    if (selectedField.value === 'date') {
        let startDate = document.getElementById('startDate').value;
        let endDate = document.getElementById('endDate').value;
        //console.log("Start Date:", startDate);
        //console.log("End Date:", endDate);
        sqlQuery = `SELECT * FROM ${tableName} WHERE ${dateField} BETWEEN '${startDate}' AND '${endDate}'`;
<<<<<<< HEAD
    }else if (selectedField === 'all') {
        sqlQuery = `SELECT * FROM ${tableName}`; // Sélectionner tous les utilisateurs
    } else if (selectedField) { 
        let conditionValue = document.getElementById('conditionValue').value;
        //console.log("Condition Value:", conditionValue);
        sqlQuery = `SELECT * FROM ${tableName} WHERE ${selectedField} = '${conditionValue}'`;
=======
    } else if (selectedField.value) {
        let conditionValue = document.getElementById('conditionValue').value;
        console.log("Condition Value:", conditionValue);
        sqlQuery = `SELECT * FROM ${tableName} WHERE ${selectedField.value} = '${conditionValue}'`;
>>>>>>> 50d68ed (Amelioration du code & Ajout de la requête fetch pour communiquer avec le fichier execute_query.php)
    }

    console.log("Generated SQL Query:", sqlQuery);

    return sqlQuery;
}

/**
 * 
 * @param {boolean} enable 
 */
function toggleExecuteButton(enable = true) {
    if (executeButton === null) {
        return;
    }

<<<<<<< HEAD
=======
>>>>>>> main
function checkInput() {
    const inputs = document.querySelectorAll('#conditionInputs input');
    const allFilled = Array.from(inputs).every(input => input.value.trim() !== '');
    const selectedField = document.getElementById('fieldSelect').value;
    const executeBtn = document.getElementById('executeBtn');
    const previewBtn = document.getElementById('previewSqlBtn');

    if (selectedField && allFilled) {
        executeBtn.removeAttribute('disabled');
        executeBtn.classList.remove('inactive');
        previewBtn.style.opacity = 1;
        previewBtn.style.display = 'block';
        previewBtn.classList.remove('inactive');
    } else if (selectedField== 'all'){
        executeBtn.removeAttribute('disabled');
        executeBtn.classList.remove('inactive');
        previewBtn.style.opacity = 1;
        previewBtn.style.display = 'block';
        previewBtn.classList.remove('inactive');
    }else {
        executeBtn.setAttribute('disabled', 'disabled');
        executeBtn.classList.add('inactive');
        previewBtn.style.opacity = 0;
        setTimeout(() => {
            previewBtn.style.display = 'none';
        }, 300);
        previewBtn.classList.add('inactive');
=======
    if (enable) {
        executeButton.removeAttribute('disabled');
        executeButton.classList.remove('inactive');
    } else {
        executeButton.setAttribute('disabled', 'disabled');
        executeButton.classList.add('inactive');
>>>>>>> 50d68ed (Amelioration du code & Ajout de la requête fetch pour communiquer avec le fichier execute_query.php)
    }
}

/**
 * 
 * @param {Event} event 
 * @returns 
 */
function executeRequest(event) {
    event.preventDefault();
    event.stopPropagation();

    if (sqlQuery == null || sqlQuery == '') {
        generateSqlQuery();
        if (sqlQuery == null || sqlQuery == '') {
            alert("Aucune requête n'a été construite.")
            return;
        }
    }

<<<<<<< HEAD
    // Réinitialiser l'état des boutons à leur état par défaut
    executeBtn.setAttribute('disabled', 'disabled');
    executeBtn.classList.add('inactive');
    setTimeout(() => {
    previewBtn.style.display = 'none';
    }, 300);
    previewBtn.style.display = 'none';
    previewBtn.classList.add('inactive');
    previewBtn.style.opacity = 0;
    //document.getElementById('bouton1').disabled = false;
    //document.getElementById('bouton2').disabled = true;
}
<<<<<<< HEAD
function executeQuery(sqlQuery) {
    $.ajax({
        url: 'execute_query.php', // Chemin vers le script PHP qui exécutera la requête SQL
        method: 'POST',
        data: { sqlQuery: sqlQuery },
        dataType: 'json',
        success: function(response) {
            displayResults(response);
        },
        error: function(xhr, status, error) {
            console.error('Erreur lors de l\'exécution de la requête SQL :', error);
        }
    });
}

function displayResults(results) {
    const tableBody = $('#resultTableBody');
    tableBody.empty(); // Nettoyer le contenu précédent du tableau

    $.each(results, function(index, row) {
        const tr = $('<tr>');
        $.each(row, function(key, value) {
            tr.append($('<td>').text(value));
        });
        tableBody.append(tr);
    });

    $('#resultTable').show(); // Afficher le tableau des résultats
}

// Appel à la fonction executeQuery avec la requête SQL générée
$('#executeBtn').click(function() {
    const selectedField = $('#fieldSelect').val();
    const sqlQuery = generateSqlQuery(selectedField);
    executeQuery(sqlQuery);
});

=======
=======



sqlQuery = '';
function generateSqlQuery(selectedField) {
    //console.log("Selected Field:", selectedField);

    const tableName = 'facebook_infos.users';
    const dateField = 'date';

    
    if (selectedField === 'date') {
        let startDate = document.getElementById('startDate').value;
        let endDate = document.getElementById('endDate').value;
        //console.log("Start Date:", startDate);
        //console.log("End Date:", endDate);
        sqlQuery = `SELECT * FROM ${tableName} WHERE ${dateField} BETWEEN '${startDate}' AND '${endDate}'`;
    }else if (selectedField === 'all') {
        sqlQuery = `SELECT * FROM ${tableName}`; // Sélectionner tous les utilisateurs
    } else { 
        let conditionValue = document.getElementById('conditionValue').value;
        console.log("Condition Value:", conditionValue);
        console.log("champ selectionné", selectedField);
        sqlQuery = `SELECT * FROM ${tableName} WHERE ${selectedField} = '${conditionValue}'`;
    }

    console.log("Generated SQL Query:", sqlQuery);

    return sqlQuery;
}

/**
 * 
 * @param {boolean} enable 
 */
function toggleExecuteButton(enable = true) {
    if (executeButton === null) {
        return;
    }

    if (enable) {
        executeButton.removeAttribute('disabled');
        executeButton.classList.remove('inactive');
    } else {
        executeButton.setAttribute('disabled', 'disabled');
        executeButton.classList.add('inactive');
    }
}

/**
 * 
 * @param {Event} event 
 * @returns 
 */
function executeRequest(event) {
    const selectedField = document.getElementById('fieldSelect').value;
    event.preventDefault();
    event.stopPropagation();

    if (sqlQuery == null || sqlQuery == '') {
        sqlQuery= generateSqlQuery(selectedField);
        if (sqlQuery == null || sqlQuery == '') {
            alert("Aucune requête n'a été construite.")
            return;
        }
    }

>>>>>>> main
    if (form == null) {
        return;
    }

    const formData = new FormData(form);
<<<<<<< HEAD
    const url = '/execute_query.php';
=======
    const url = '/dropdown_sql/execute_query.php';
>>>>>>> main
    const options = {
        method: 'POST',
        body: formData,
    };
    fetch(url, options)
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch(error => {
            console.error('Error submitting form:', error);
        })
        .finally();
}

/**
 * 
 * @param {Array} array 
 */
function arrayToHtmlTable(array) {
    // Flemme de faire
}
<<<<<<< HEAD
>>>>>>> 50d68ed (Amelioration du code & Ajout de la requête fetch pour communiquer avec le fichier execute_query.php)
=======
    document.getElementById('btnModifier').addEventListener('click', function() {
        var sqlCodeElement = document.getElementById('sqlCode');
        var btnActions = document.getElementById('btnActions');
        var modifbutton=  document.getElementById('btnModifier');
        modifbutton.style.display= 'none';
        
        sqlCodeElement.contentEditable = true;
        sqlCodeElement.focus();
        btnActions.style.display = 'block';
    });
    
    document.getElementById('btnValider').addEventListener('click', function() {
        var sqlCodeElement = document.getElementById('sqlCode');
        sqlQuery= sqlCodeElement.innerText;
        var btnActions = document.getElementById('btnActions');
        var modifbutton=  document.getElementById('btnModifier');
        modifbutton.style.display= 'block';
        
        sqlCodeElement.contentEditable = false;
        btnActions.style.display = 'none';
    });
    
    document.getElementById('btnAnnuler').addEventListener('click', function() {
        var sqlCodeElement = document.getElementById('sqlCode');
        var btnActions = document.getElementById('btnActions');
        var modifbutton=  document.getElementById('btnModifier');
        modifbutton.style.display= 'block';
        sqlCodeElement.contentEditable = false;
        sqlCodeElement.innerText = sqlQuery; // Réinitialiser le contenu
        btnActions.style.display = 'none';
    });

    $(document).ready(function() {
        $('#executeBtn').click(function() {
            //var maVariable = 'Valeur à envoyer à PHP';
            
            $.ajax({
                url: 'traitement.php',
                method: 'POST',
                data: { variableJS: sqlQuery },
                success: function(response) {
                    $('#resultat').html('Réponse de PHP : ' + response);
                },
                error: function() {
                    $('#resultat').html('Une erreur s\'est produite lors de la communication avec PHP.');
                }
            });
        });
    });
    
        
>>>>>>> main
