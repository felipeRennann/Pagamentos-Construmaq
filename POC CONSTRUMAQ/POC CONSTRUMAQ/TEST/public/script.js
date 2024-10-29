
    function showTab(tab) {
        
        const tabs = document.querySelectorAll('.tab');
        tabs.forEach(t => {
            t.classList.remove('active');
        });
        document.getElementById(tab).classList.add('active');
    }


    document.addEventListener('DOMContentLoaded', () => {
        console.log("DOM carregado, buscando cargos...");
        fetchCargos();
        showTab('lista'); // Mostra a aba de cargos ao carregar
    });

    async function fetchCargos() {
        try {
            const response = await fetch('http://127.0.0.1:5000/api/cargos'); 
            if (!response.ok) throw new Error('Network response was not ok');
            const cargos = await response.json();
            
            
            console.log("Cargos recebidos da API:", cargos); 
            
            const cargoSelect = document.getElementById('cargo_funcionario');
            const listaCargos = document.getElementById('lista-cargos');

            console.log("Elemento cargo_funcionario:", cargoSelect);
            console.log("Elemento lista-cargos:", listaCargos);

            cargoSelect.innerHTML = ''; // Limpa as opções existentes
            listaCargos.innerHTML = ''; // Limpa a lista existente
            //listaCargos.appendChild(table); // Adiciona a tabela ao elemento


            
            // Cria uma tabela dinamicamente
            const table = document.createElement('table');
            table.style.width = '100%'; // Ajusta a largura da tabela
            table.innerHTML = `
                <thead>
                    <tr>
                        <th>Cargo</th>
                        <th>Hora Base (%)</th>
                        <th>Repouso Remunerado (%)</th>
                        <th>Hora Extra 50%</th>
                        <th>Hora Extra 100%</th>
                        <th>Adicional Noturno (%)</th>
                        <th>Ferias (%)</th>
                        <th>Pagamento 1/3 Ferias (%)</th>
                        <th>Pagamaneto 13° Salario (%)</th>
                        <th>Pagamento FGTS (%)</th>
                        <th>Desconto INSS (%)</th>
                        <th>Desconto Refeição (%)</th>
                        <th>Desconto Vale Transporte (%)</th>
                    </tr>
                </thead>
                <tbody></tbody>
            `;
            
            const tableBody = table.querySelector('tbody');
            
            // Itera sobre as chaves do objeto cargos
            for (const key in cargos) {
                if (cargos.hasOwnProperty(key)) {
                    const cargo = cargos[key];  
                    console.log("Preenchendo cargo:", key, cargo); // Adicione este log

                    // Preenche a tabela com os dados do cargo
                    const row = tableBody.insertRow();
            row.insertCell(0).innerText = key; // Cargo
            row.insertCell(1).innerText = (parseFloat(cargo.valor_hora_base) || 0).toFixed(2); // Valor Hora Base
            row.insertCell(2).innerText = (parseFloat(cargo.repouso_remunerado) || 0).toFixed(2); // Vl. Repouso Remunerado
            row.insertCell(3).innerText = (parseFloat(cargo.valor_hora_extra_um) || 0).toFixed(2); // Valor Hora Extra de 50%
            row.insertCell(4).innerText = (parseFloat(cargo.valor_hora_extra_dois) || 0).toFixed(2); // Valor Hora Extra de 100%
            row.insertCell(5).innerText = (parseFloat(cargo.adicional_noturno) || 0).toFixed(2); // Vl. Ad. Noturno
            row.insertCell(6).innerText = (parseFloat(cargo.valor_ferias) || 0).toFixed(2); // Valor Férias
            row.insertCell(7).innerText = (parseFloat(cargo.valor_um_terco_ferias) || 0).toFixed(2); // 1/3 Férias
            row.insertCell(8).innerText = (parseFloat(cargo.valor_decimo_terceiro) || 0).toFixed(2); // 13º Salário
            row.insertCell(9).innerText = (parseFloat(cargo.pagamento_fgts) || 0).toFixed(2); // Pagamento FGTS
            row.insertCell(10).innerText = (parseFloat(cargo.desconto_inss) || 0).toFixed(2); // Desconto INSS
            row.insertCell(11).innerText = (parseFloat(cargo.desconto_refeicao) || 0).toFixed(2); // Desconto Refeição
            row.insertCell(12).innerText = (parseFloat(cargo.desconto_transporte) || 0).toFixed(2); // Desconto Transporte

                    // Preenche o select com as opções de cargos
                    const option = document.createElement('option');
                    option.value = key;
                    option.textContent = key;
                    cargoSelect.appendChild(option);
                }
            }
            
            // Exibe a tabela na página (assumindo que você tenha um elemento para isso)
            listaCargos.appendChild(table);
            console.log("Tabela adicionada ao DOM:", table); // Adicione este log

        } catch (error) {
            console.error("Erro ao buscar cargos:", error);
        }
    }

    // Criar cargo 
    document.getElementById('cargo-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário



    const formData = new FormData(event.target);
    //const cargoData = Object.fromEntries(formData);

    const cargoData = {
    nome_cargo: document.getElementById('nome_cargo').value.trim(),
    valor_hora_base: parseFloat(document.getElementById('valor_hora_base').value),
    valor_hora_extra_um: parseFloat(document.getElementById('valor_hora_extra_um').value),
    valor_hora_extra_dois: parseFloat(document.getElementById('valor_hora_extra_dois').value),
    adicional_noturno: parseFloat(document.getElementById('adicional_noturno').value),
    repouso_remunerado: parseFloat(document.getElementById('repouso_remunerado').value),
    desconto_inss: parseFloat(document.getElementById('desconto_inss').value),
    desconto_refeicao: parseFloat(document.getElementById('desconto_refeicao').value),
    desconto_transporte: parseFloat(document.getElementById('desconto_transporte').value),
    pagamento_fgts: parseFloat(document.getElementById('pagamento_fgts').value),
    valor_decimo_terceiro: parseFloat(document.getElementById('valor_decimo_terceiro').value),
    valor_ferias: parseFloat(document.getElementById('valor_ferias').value),
    valor_um_terco_ferias: parseFloat(document.getElementById('valor_um_terco_ferias').value),
    };


    // Log do cargoData
    console.log('Dados do Cargo:', cargoData); // Aqui está o log


    const numericFields = [
    'valor_hora_base',
    'valor_hora_extra_um',
    'valor_hora_extra_dois',
    'adicional_noturno',
    'repouso_remunerado',
    'desconto_inss',
    'desconto_refeicao',
    'desconto_transporte',
    'pagamento_fgts',
    'valor_decimo_terceiro',
    'valor_ferias',
    'valor_um_terco_ferias'
    ];

    // Captura os dados do formulário
    numericFields.forEach(field => {    
    cargoData[field] = parseFloat(cargoData[field]) || 0; // Corrigido para usar 'field'
    });

    console.log(cargoData.nome_cargo); 
    console.log(cargoData);
    console.log(typeof cargoData.valor_hora_base); // Deve ser 'number'

    // Envie os dados para o backend
    try{
    const response = await fetch('http://127.0.0.1:5000/api/cargos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(cargoData)
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById('message').textContent = data.message;  // Mensagem de sucesso
        fetchCargos();  // Atualiza a lista de cargos
        messageDiv.textContent = data.message; // Mensagem de sucesso
        messageDiv.style.display = 'block'; // Mostra a mensagem


        // Ocultar a mensagem após 5 segundos e recarregar a página
        setTimeout(() => {
            messageDiv.style.display = 'none'; // Esconde a mensagem
            location.reload(); // Recarrega a página
        }, 5000); // 5000 milissegundos = 5 segundos

    } else {
        const error = await response.json();
        document.getElementById('message').textContent = error.message;  // Mensagem de erro
        messageDiv.style.display = 'block'; // Mostra a mensagem de erro
    }
    } catch (error) {
        console.error('Erro ao enviar os dados:', error);
        messageDiv.textContent = 'Erro ao enviar os dados. Tente novamente.';
        messageDiv.style.display = 'block'; // Mostra a mensagem de erro
    }

    });




    // Cadastro para pagamento e imprimir PDF -> Gerador do PDF
    document.getElementById('gerarDocumentoButton').addEventListener('click', async function(event) {
    event.preventDefault();
    const formData = new FormData(document.getElementById('funcionario-form'));
    const funcionarioData = Object.fromEntries(formData);

    const cargoSelect = document.getElementById('cargo_funcionario');
    const cargoId = cargoSelect.value;

    // Fetch para obter os dados do cargo
    const cargoResponse = await fetch(`http://127.0.0.1:5000/api/cargos/${cargoId}`);
    if (!cargoResponse.ok) {
    console.error('Erro ao buscar dados do cargo:', cargoResponse.statusText);
    return;
    }
    const cargo = await cargoResponse.json();

    //Definir um valor default em caso de valor zerado ou null
    const checkAndParse = (value) => {  
    const parsedValue = parseFloat(value);
    return isNaN(parsedValue) ? 0.00 : parsedValue;
    };

    // Função para formatar data para DD-MM-YYYY
    const formatDate = (dateString) => {
    const [year, month, day] = dateString.split('-');
    return `${day}-${month}-${year}`; // Formato DD/MM/YYYY
    };

    // Adicione os dados do cargo ao objeto funcionarioData

    funcionarioData.horas_trabalhadas = checkAndParse(funcionarioData.horas_trabalhadas, 10,);
    funcionarioData.horas_extras_um = checkAndParse(funcionarioData.horas_extras_um, 10);
    funcionarioData.horas_extras_dois = checkAndParse(funcionarioData.horas_extras_dois, 10);
    funcionarioData.horas_noturnas = checkAndParse(funcionarioData.horas_noturnas, 10);
    funcionarioData.repouso_remunerado = checkAndParse(funcionarioData.repouso_remunerado, 10);
    funcionarioData.desc_refeicao= checkAndParse(funcionarioData.desc_refeicao, 10);
    funcionarioData.correcao_positiva = checkAndParse(funcionarioData.correcao_positiva, 10);
    funcionarioData.correcao_negativa = checkAndParse(funcionarioData.correcao_negativa, 10);
    funcionarioData.data_inicio = formatDate(funcionarioData.data_inicio);
    funcionarioData.data_fim = formatDate(funcionarioData.data_fim);

    // Verifique se todos os campos obrigatórios estão preenchidos
    const requiredFields = ['data_inicio','data_fim','nome_funcionario', 'horas_trabalhadas', 'repouso_remunerado', 'horas_extras_um', 'horas_extras_dois', 'horas_noturnas', 'desc_refeicao', 'correcao_positiva', 'correcao_negativa'];

    console.log(" Dado enviados ",funcionarioData.repouso_remunerado); 
    console.log(" Dado enviados 3 ",funcionarioData.data_inicio); 


    //Valida os dados enviados -> Valor fucionario === string // Demais tem que ser float.
    for (const field of requiredFields) {
    const value = funcionarioData[field];
    // Verifica se o campo é nome_funcionario
    if (field === 'nome_funcionario') {
    if (typeof value !== 'string' || value.trim() === '') {
        console.error(`Campo obrigatório "${field}" é inválido.`);
        return;
    }
    } 

    // Verifica se o campo é data_inicio ou data_fim
    else if (field === 'data_inicio' || field === 'data_fim') {
    if (!value || new Date(value.split('-').reverse().join('-')).toString() === "Invalid Date") {
        const errorMessage = `Preenchimento do campo "${field}" é obrigatorio!.`;
        console.error(errorMessage);

        
        // Exibir a mensagem de erro no front-end
        const errorElement = document.getElementById('error-message');
        errorElement.textContent = errorMessage; // Define o texto da mensagem
        errorElement.style.display = 'block'; // Torna a mensagem visível

                // Ocultar a mensagem após 5 segundos
        setTimeout(() => {
            errorElement.style.display = 'none'; // Esconde a mensagem
        }, 5000); 

        return;
    }
    }

    // Para outros campos que são numéricos
    else {
    if (value === undefined || value === null || isNaN(value)) {
        console.error(`Campo obrigatório "${field}" é inválido.`);
        return;
    }
    }

    }   console.log(funcionarioData)
    console.log('Dados do funcionário antes de enviar:', JSON.stringify(funcionarioData, null, 2));

    // Envie os dados para o backend
    const response = await fetch('http://127.0.0.1:5000/api/criar_funcionario', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(funcionarioData),
    mode:'cors'

    });
    console.log('Dados do funcionário antes de enviar:', funcionarioData);

    if (response.ok) {
    // Ler o PDF como blob
    const blob = await response.blob();

    // Cria um link para download do PDF
    const url = window.URL.createObjectURL(blob);
    const iframe = document.createElement('iframe');
    iframe.style.width = '100%';
    iframe.style.height = '600px';
    iframe.src = url;
    document.getElementById('documentContentPreview').innerHTML = ''; // Limpar conteúdo anterior
    document.getElementById('documentContentPreview').appendChild(iframe);



    // Configura o evento de clique no botão de imprimir PDF
    document.getElementById('printDocumentButton').onclick = async function() { 
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${funcionarioData.nome_funcionario}_olerite.pdf`;
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
    };
    

    // Configura o evento de clique no botão "Cancelar"
    document.querySelector('.btn-secondary[data-bs-dismiss="modal"]').onclick = function() {
        $('#documentPreviewModal').modal('hide'); // Fecha o modal
    };
    // Exibe o modal se necessário
    $('#documentPreviewModal').modal('show');

    } else {
        console.error('Erro ao gerar o olerite:', response.statusText);
    }
        
    });
    // Fechar mensagens 
    messageDiv.addEventListener('click', function() {
    messageDiv.style.display = 'none'; // Esconde a mensagem ao clicar na mensagem
    location.reload(); // Recarrega a página ao fechar a mensagem
    });

