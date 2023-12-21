// Substitua as URLs pelos endpoints reais das suas APIs
const avaliacoesEndpoint = 'http://localhost:4000/avaliacoes';
const diretoriasEndpoint = 'http://localhost:4000/diretorias';
const entregasEndpoint = 'http://localhost:4000/entregas';
const transportadorasEndpoint = 'http://localhost:4000/transportadoras';

// Função para verificar se um valor é um objeto
const isObject = (value) => typeof value === 'object' && value !== null;

// Função para criar e exibir uma tabela com dados dinâmicos
function displayDataInTable(elementId, data) {
    const table = document.createElement('table');
    table.setAttribute('border', '1');

    // Cria a linha de cabeçalho
    const headerRow = document.createElement('tr');
    for (const key in data[0]) {
        const headerCell = document.createElement('th');
        headerCell.innerText = key;
        headerRow.appendChild(headerCell);
    }
    table.appendChild(headerRow);

    // Função para criar uma célula de dados com verificação de objeto
    const createDataCell = (value) => {
        const dataCell = document.createElement('td');
        dataCell.innerText = isObject(value) ? 'Expandir' : value;
        if (isObject(value)) {
            dataCell.classList.add('expandable-cell');
            dataCell.style.cursor = 'pointer';
            dataCell.style.textDecoration = 'underline';
            dataCell.addEventListener('click', () => toggleExpansion(dataCell, value));
        }
        return dataCell;
    };

    // Cria as linhas de dados
    data.forEach(item => {
        const dataRow = document.createElement('tr');
        for (const key in item) {
            const dataCell = createDataCell(item[key]);
            dataRow.appendChild(dataCell);
        }
        table.appendChild(dataRow);

        // Adiciona uma linha adicional para exibir os detalhes (inicialmente oculta)
        const detailsRow = document.createElement('tr');
        detailsRow.className = 'details-row';
        detailsRow.style.display = 'none';

        const detailsCell = document.createElement('td');
        detailsCell.colSpan = Object.keys(item).length; // Colspan abrange todas as colunas
        detailsCell.innerHTML = '<strong>Detalhes:</strong><br>' + getDetailsList(item);
        detailsRow.appendChild(detailsCell);
        table.appendChild(detailsRow);
    });

    // Obtém o elemento pelo ID e adiciona a tabela como um filho
    const element = document.getElementById(elementId);
    element.innerHTML = ''; // Limpa o conteúdo existente
    element.appendChild(table);
}

// Função para alternar a visibilidade da linha de detalhes ao clicar na célula expansível
function toggleExpansion(cell, item) {
    const row = cell.parentElement;
    const detailsRow = row.nextElementSibling;

    if (detailsRow && detailsRow.classList.contains('details-row')) {
        detailsRow.style.display = detailsRow.style.display === 'none' ? 'table-row' : 'none';
    }
}

// Função para obter uma lista formatada de detalhes
function getDetailsList(item) {
    return Object.entries(item)
        .map(([key, value]) => `<strong>${key}:</strong> ${isObject(value) ? JSON.stringify(value) : value}`)
        .join('<br>');
}

// Exemplos de uso
async function getTransportadoras() {
    try {
        const response = await axios.get(transportadorasEndpoint);
        displayDataInTable('dataBody', response.data); // Corrigido para 'dataBody'
    } catch (error) {
        console.error('Erro ao obter transportadoras:', error);
    }
}

async function getDiretorias() {
    try {
        const response = await axios.get(diretoriasEndpoint);
        displayDataInTable('dataBody', response.data); // Corrigido para 'dataBody'
    } catch (error) {
        console.error('Erro ao obter diretorias:', error);
    }
}

async function getEntregas() {
    try {
        const response = await axios.get(entregasEndpoint);
        displayDataInTable('dataBody', response.data); // Corrigido para 'dataBody'
    } catch (error) {
        console.error('Erro ao obter entregas:', error);
    }
}

async function getAvaliacoes() {
    try {
        const response = await axios.get(avaliacoesEndpoint);
        displayDataInTable('dataBody', response.data); // Corrigido para 'dataBody'
    } catch (error) {
        console.error('Erro ao obter avaliações:', error);
    }
}
