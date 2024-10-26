
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
        document.getElementById('name_funcionario').value = '';
        showTab('lista'); // Mostra a aba de cargos ao carregar
    });
    

    async function fetchCargos() {
        try {
            const response = await fetch('http://127.0.0.1:5000/api/funcionarios'); 
            if (!response.ok) throw new Error('Network response was not ok');
            const funcionarios = await response.json();
            console.log("Cargos recebidos da API teste:", funcionarios);
        
            
            const funcionarioSelect = document.getElementById('name_funcionario');
            const listaFuncionarios = document.getElementById('lista-funcionarios');

            console.log("Elemento name_funcionario:", funcionarioSelect);
            console.log("Elemento lista-funcionarios:", listaFuncionarios);

            funcionarioSelect.innerHTML = ''; // Limpa as opções existentes
            listaFuncionarios.innerHTML = ''; // Limpa a lista existente
            //listaCargos.appendChild(table); // Adiciona a tabela ao elemento


            
            // Cria uma tabela dinamicamente
            const table = document.createElement('table');
            table.style.width = '100%'; // Ajusta a largura da tabela
            table.innerHTML = `
                <thead>
                    <tr>
                        <th>Funcionario</th>
                        <th>CPF</th>
                        <th>Chave PIX</th>
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
            for (const key in funcionarios) {
                if (funcionarios.hasOwnProperty(key)) {
                    const funcionario = funcionarios[key];  
                    console.log("Preenchendo Funcionarios", key, funcionario); // Adicione este log

                    // Preenche a tabela com os dados do cargo
                    const row = tableBody.insertRow();
            row.insertCell(0).innerText = key; // funcionario
            row.insertCell(1).innerText = funcionario.numero_cpf;
            row.insertCell(2).innerText = funcionario.chave_pix;
            row.insertCell(3).innerText = (parseFloat(funcionario.valor_hora_base) || 0).toFixed(2); // Valor Hora Base
            row.insertCell(4).innerText = (parseFloat(funcionario.repouso_remunerado) || 0).toFixed(2); // Vl. Repouso Remunerado
            row.insertCell(5).innerText = (parseFloat(funcionario.valor_hora_extra_um) || 0).toFixed(2); // Valor Hora Extra de 50%
            row.insertCell(6).innerText = (parseFloat(funcionario.valor_hora_extra_dois) || 0).toFixed(2); // Valor Hora Extra de 100%
            row.insertCell(7).innerText = (parseFloat(funcionario.adicional_noturno) || 0).toFixed(2); // Vl. Ad. Noturno
            row.insertCell(8).innerText = (parseFloat(funcionario.valor_ferias) || 0).toFixed(2); // Valor Férias
            row.insertCell(9).innerText = (parseFloat(funcionario.valor_um_terco_ferias) || 0).toFixed(2); // 1/3 Férias
            row.insertCell(10).innerText = (parseFloat(funcionario.valor_decimo_terceiro) || 0).toFixed(2); // 13º Salário
            row.insertCell(11).innerText = (parseFloat(funcionario.pagamento_fgts) || 0).toFixed(2); // Pagamento FGTS
            row.insertCell(12).innerText = (parseFloat(funcionario.desconto_inss) || 0).toFixed(2); // Desconto INSS
            row.insertCell(13).innerText = (parseFloat(funcionario.desconto_refeicao) || 0).toFixed(2); // Desconto Refeição
            row.insertCell(14).innerText = (parseFloat(funcionario.desconto_transporte) || 0).toFixed(2); // Desconto Transporte

                     
                    // Preenche o select com as opções de cargos
                    const option = document.createElement('option');
                    option.value =key;
                    option.textContent =key;
                    funcionarioSelect.appendChild(option);
                    console.log("dados chegando", key, funcionario); // Adicione este log

                    // Log atualizado para verificar se as opções foram criadas corretamente
                    ;console.log(`Criando option para o funcionário com chave: ${key}`, {
                        id: option.value,
                        nome: option.textContent
                    })

                    // Adiciona botão de editar
                    const actionsCell = row.insertCell(15);
                    const editButton = document.createElement('button');
                    editButton.textContent = 'Editar';
                    editButton.onclick = () =>  {
                        const nomeFuncionario = key; // Nome do funcionário
                        const cpfFuncionario = funcionario.numero_cpf; // CPF do funcionário
                        const chavePix = funcionario.chave_pix
                        const valorHoraBase = funcionario.valor_hora_base
                        const valorHoraExtraUm = funcionario.valor_hora_extra_um
                        const valorHoraExtraDois = funcionario.horas_extras_dois
                        const adicionalNoturno = funcionario.adicional_noturno
                        const repousoRemunerado = funcionario.repouso_remunerado
                        const valorFerias = funcionario.valor_ferias
                        const valorUmTercoFerias = funcionario.valor_um_terco_ferias
                        const valorDecimoTerceiro = funcionario.valor_decimo_terceiro
                        const pagamentoFgts = funcionario.pagamento_fgts
                        const descontoInss = funcionario.desconto_inss
                        const descontoRefeicao = funcionario.desconto_refeicao
                        const descontoTransporte = funcionario.desconto_transporte

                        editarFuncionarioModal(nomeFuncionario, cpfFuncionario, chavePix,valorHoraBase, 
                            valorHoraExtraUm, valorHoraExtraDois,adicionalNoturno, repousoRemunerado, 
                            valorFerias, valorUmTercoFerias, valorDecimoTerceiro, pagamentoFgts, 
                            descontoInss, descontoRefeicao, descontoTransporte);
                    }
                    
                    actionsCell.appendChild(editButton);
                }
            }
            

            // Exibe a tabela na página (assumindo que você tenha um elemento para isso)
            
            listaFuncionarios.appendChild(table);
            console.log("Tabela adicionada ao DOM:", table); // Adicione este log

        } catch (error) {
            console.error("Erro ao buscar cargos:", error);
        }
    }
                
        // Função para filtrar os funcionários pelo nome e cpf
        function filterFuncionarios() {
            const searchValue = document.getElementById('search-funcionario').value.toLowerCase();
            const rows = document.querySelectorAll('#lista-funcionarios table tbody tr');

            rows.forEach(row => {
                const nomeFuncionario = row.cells[0].innerText.toLowerCase();
                const cpfFuncionario = row.cells[1].innerText.toLowerCase();
                row.style.display = nomeFuncionario.includes(searchValue) || cpfFuncionario.includes(searchValue) ? '' : 'none'
            });
        }
 
    let isEditMode = false;    
    // Editar Funcionario 
    function editarFuncionarioModal(nomeFuncionario, cpfFuncionario, chavePix, valorHoraBase, valorHoraExtraUm,  
        valorHoraExtraDois, adicionalNoturno, repousoRemunerado, valorFerias, valorUmTercoFerias, valorDecimoTerceiro,
         pagamentoFgts, descontoInss, descontoRefeicao, descontoTransporte ) {
        // Abrir o modal
        
        const modal = document.getElementById('editModal');
        modal.style.display = 'block';

        // Preencher os campos do modal com os dados do funcionário
        document.getElementById('nome_funcionario').value = nomeFuncionario;
        document.getElementById('numero_cpf').value = cpfFuncionario; // CPF do funcionário
        document.getElementById('chave_pix').value = chavePix; // Chave PIX
        document.getElementById('valor_hora_base').value = (parseFloat(valorHoraBase) || 0).toFixed(2); // Valor Hora Base
        document.getElementById('valor_hora_extra_um').value = (parseFloat(valorHoraExtraUm) || 0).toFixed(2); // Hora Extra 50%
        document.getElementById('valor_hora_extra_dois').value = (parseFloat(valorHoraExtraDois) || 0).toFixed(2); // Hora Extra 100%
        document.getElementById('adicional_noturno').value = (parseFloat(adicionalNoturno) || 0).toFixed(2); // Adicional Noturno
        document.getElementById('repouso_remunerado').value = (parseFloat(repousoRemunerado) || 0).toFixed(2); // Repouso Remunerado
        document.getElementById('valor_ferias').value = (parseFloat(valorFerias) || 0).toFixed(2); // Férias
        document.getElementById('valor_um_terco_ferias').value = (parseFloat(valorUmTercoFerias) || 0).toFixed(2); // 1/3 Férias
        document.getElementById('valor_decimo_terceiro').value = (parseFloat(valorDecimoTerceiro) || 0).toFixed(2); // 13º Salário
        document.getElementById('pagamento_fgts').value = (parseFloat(pagamentoFgts) || 0).toFixed(2); // FGTS
        document.getElementById('desconto_inss').value = (parseFloat(descontoInss) || 0).toFixed(2); // INSS
        document.getElementById('desconto_refeicao').value = (parseFloat(descontoRefeicao) || 0).toFixed(2); // Refeição
        document.getElementById('desconto_transporte').value = (parseFloat(descontoTransporte) || 0).toFixed(2); // Transporte
        
        
        // Armazenar o ID do funcionário no formulário para edição
        //document.getElementById('funcionario-form').setAttribute('data-id', nomeFuncionario);
        let isEditMode = false;    

        // Editar Funcionário 
        function editarFuncionarioModal(nomeFuncionario, cpfFuncionario, chavePix, valorHoraBase, valorHoraExtraUm,  
            valorHoraExtraDois, adicionalNoturno, repousoRemunerado, valorFerias, valorUmTercoFerias, valorDecimoTerceiro,
             pagamentoFgts, descontoInss, descontoRefeicao, descontoTransporte ) {
            
            // Abrir o modal
            const modal = document.getElementById('editModal');
            modal.style.display = 'block';
        
            // Preencher os campos do modal com os dados do funcionário
            document.getElementById('nome_funcionario').value = nomeFuncionario;
            document.getElementById('numero_cpf').value = cpfFuncionario; // CPF do funcionário
            document.getElementById('chave_pix').value = chavePix; // Chave PIX
            document.getElementById('valor_hora_base').value = (parseFloat(valorHoraBase) || 0).toFixed(2); // Valor Hora Base
            document.getElementById('valor_hora_extra_um').value = (parseFloat(valorHoraExtraUm) || 0).toFixed(2); // Hora Extra 50%
            document.getElementById('valor_hora_extra_dois').value = (parseFloat(valorHoraExtraDois) || 0).toFixed(2); // Hora Extra 100%
            document.getElementById('adicional_noturno').value = (parseFloat(adicionalNoturno) || 0).toFixed(2); // Adicional Noturno
            document.getElementById('repouso_remunerado').value = (parseFloat(repousoRemunerado) || 0).toFixed(2); // Repouso Remunerado
            document.getElementById('valor_ferias').value = (parseFloat(valorFerias) || 0).toFixed(2); // Férias
            document.getElementById('valor_um_terco_ferias').value = (parseFloat(valorUmTercoFerias) || 0).toFixed(2); // 1/3 Férias
            document.getElementById('valor_decimo_terceiro').value = (parseFloat(valorDecimoTerceiro) || 0).toFixed(2); // 13º Salário
            document.getElementById('pagamento_fgts').value = (parseFloat(pagamentoFgts) || 0).toFixed(2); // FGTS
            document.getElementById('desconto_inss').value = (parseFloat(descontoInss) || 0).toFixed(2); // INSS
            document.getElementById('desconto_refeicao').value = (parseFloat(descontoRefeicao) || 0).toFixed(2); // Refeição
            document.getElementById('desconto_transporte').value = (parseFloat(descontoTransporte) || 0).toFixed(2); // Transporte
        
            isEditMode = true;  // Marca o modal como modo de edição
        }
        
        // Função para fechar o modal
        document.querySelector('.close').onclick = function() {
            document.getElementById('editModal').style.display = 'none';
            isEditMode = false;  // Reseta o modo de edição
        }
        
        // Função para salvar as edições do funcionário
        document.getElementById('editForm').addEventListener('submit', async function(event) {
            event.preventDefault(); // Impede o envio padrão do formulário
        
            const nomeFuncionario = document.getElementById('nome_funcionario').value.trim(); // Obtém o nome do funcionário
            const formData = {
                numero_cpf: document.getElementById('numero_cpf').value.trim(),
                chave_pix: document.getElementById('chave_pix').value.trim(),
                valor_hora_base: parseFloat(document.getElementById('valor_hora_base').value),
                valor_hora_extra_um: parseFloat(document.getElementById('valor_hora_extra_um').value),
                valor_hora_extra_dois: parseFloat(document.getElementById('valor_hora_extra_dois').value),
                adicional_noturno: parseFloat(document.getElementById('adicional_noturno').value),
                repouso_remunerado: parseFloat(document.getElementById('repouso_remunerado').value),
                valor_ferias: parseFloat(document.getElementById('valor_ferias').value),
                valor_um_terco_ferias: parseFloat(document.getElementById('valor_um_terco_ferias').value),
                valor_decimo_terceiro: parseFloat(document.getElementById('valor_decimo_terceiro').value),
                pagamento_fgts: parseFloat(document.getElementById('pagamento_fgts').value),
                desconto_inss: parseFloat(document.getElementById('desconto_inss').value),
                desconto_refeicao: parseFloat(document.getElementById('desconto_refeicao').value),
                desconto_transporte: parseFloat(document.getElementById('desconto_transporte').value),
            };
        
            console.log('Dados do funcionário antes do envio:', formData);
        
            try {
                const response = await fetch(`http://127.0.0.1:5000/api/funcionario/${nomeFuncionario}`, {
                    method: 'PUT', // Alterando para PUT para atualização
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });
        
                if (!response.ok) {
                    let errorMessage;
                    try {
                        const error = await response.json();
                        errorMessage = error.message || 'Erro desconhecido';
                    } catch (jsonError) {
                        errorMessage = await response.text();
                    }
        
                    alert(`Erro: ${errorMessage}`);
                    throw new Error(`Erro na atualização: ${errorMessage}`);
                }
        
                const result = await response.json();
                console.log('Sucesso:', result);
                alert('Funcionário atualizado com sucesso!');
        
                // Fechar o modal
                $('#editModal').modal('hide');
        
                // Atualizar a página
                location.reload();
        
            } catch (error) {
                console.error('Erro ao salvar os dados:', error);
                alert('Erro ao salvar os dados. Tente novamente.');
            }
        })

    // Criar Funcionario 
    document.getElementById('funcionario-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    const formData = new FormData(event.target);    
    //const cargoData = Object.fromEntries(formData);

    const funcionariData = {
    nome_funcionario: document.getElementById('nome_funcionario_c').value.trim(),
    numero_cpf: document.getElementById('numero_cpf_c').value.trim(),
    chave_pix: document.getElementById('chave_pix_c').value.trim(),
    valor_hora_base: parseFloat(document.getElementById('valor_hora_base_c').value),
    valor_hora_extra_um: parseFloat(document.getElementById('valor_hora_extra_um_c').value),
    valor_hora_extra_dois: parseFloat(document.getElementById('valor_hora_extra_dois_c').value),
    adicional_noturno: parseFloat(document.getElementById('adicional_noturno_c').value),
    repouso_remunerado: parseFloat(document.getElementById('repouso_remunerado_c').value),
    desconto_inss: parseFloat(document.getElementById('desconto_inss_c').value),
    desconto_refeicao: parseFloat(document.getElementById('desconto_refeicao_c').value),
    desconto_transporte: parseFloat(document.getElementById('desconto_transporte_c').value),
    pagamento_fgts: parseFloat(document.getElementById('pagamento_fgts_c').value),
    valor_decimo_terceiro: parseFloat(document.getElementById('valor_decimo_terceiro_c').value),
    valor_ferias: parseFloat(document.getElementById('valor_ferias_c').value),
    valor_um_terco_ferias: parseFloat(document.getElementById('valor_um_terco_ferias_c').value),
    };


    // Log do cargoData
    console.log('Dados do Funcionario:',funcionariData); // Aqui está o log


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
    funcionariData[field] = parseFloat(funcionariData[field]) || 0; // Corrigido para usar 'field'
    });

    // Envie os dados para o backend
    try{
    const response = await fetch('http://127.0.0.1:5000/api/funcionarios', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(funcionariData)
    });

    if (response.ok) {
        const data = await response.json();
        document.getElementById('message').textContent = data.message;  // Mensagem de sucesso
        fetchCargos();  // Atualiza a lista de cargos

        alert('Cadastro de funcionário criado com sucesso!');
        // Atualizar a página
        location.reload();

        

    } else {
        const error = await response.json();
         alert(`Erro: ${error.message}`);
    }
    } catch (error) {
        console.error('Erro ao enviar os dados:', error);
        //alert('Erro ao enviar os dados. Tente novamente.');
        alert('Cadastro de funcionário criado com sucesso!');
        location.reload();

    }
            
            
    
    $(document).ready(function() {
        // Inicializa o Select2
        $('#name_funcionario').select2({
            placeholder: "Selecione um funcionário",
            allowClear: true,
            width: 'resolve',
            tags: true // Permite que o usuário adicione novos valores
        });
    
        // Função para carregar funcionários
        async function loadFuncionarios() {
            const response = await fetch('http://127.0.0.1:5000/api/funcionarios');
            if (!response.ok) {
                console.error('Erro ao carregar funcionários:', response.statusText);
                return;
            }
            const funcionarios = await response.json();
            
            // Se a resposta é um objeto, transforme-o em um array
            const funcionariosArray = Array.isArray(funcionarios) ? funcionarios : [funcionarios];
            
            // Preenche o select
            funcionariosArray.forEach(funcionario => {
                const option = new Option(funcionario.nome, funcionario.id, false, false);
                $('#name_funcionario').append(option);
            });
    
            // Atualiza o Select2 com os novos dados
            $('#name_funcionario').trigger('change');
        }
    
        // Carregar funcionários quando a página for carregada
        loadFuncionarios();
    });

    // Cadastro para pagamento e imprimir PDF -> Gerador do PDF
   
    document.getElementById('gerarDocumentoButton').addEventListener('click', async function(event) {
        event.preventDefault();
        alert('Fomulario enaviado ')
        console.log('Botão clicado!'); // Para verificar se está funcionando

        const formData = new FormData(document.getElementById('recibo-form'));
        const reciboData = Object.fromEntries(formData);

        console.log('Recebido do forme', formData, reciboData)

        const funcionariSelect = document.getElementById('name_funcionario');
        const funcionarioId = funcionariSelect.value;

        // Verifica se um funcionário foi selecionado
        if (!funcionarioId) {
            console.error('Por favor, selecione um funcionário.');
            return;
        }

        // Fetch para obter os dados do cargo
        const funcionarioResponse = await fetch(`http://127.0.0.1:5000/api/funcionarios/${funcionarioId}`);
        if (!funcionarioResponse.ok) {
        console.error('Erro ao buscar dados funcionario:', funcionarioResponse.statusText);
        return;
        }
        const funcionario = await funcionarioResponse.json();

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
        function checkAndParseString(value, defaultValue = "") {
            if (typeof value === "string") {
                return value.trim(); // Remove espaços em branco
            }
            return defaultValue; // Retorna um valor padrão se não for uma string
        }
        
        // Apenas adicionar os campos CPF e Chave PIX como strings ao reciboData
        reciboData.name_funcionario = checkAndParseString(reciboData.name_funcionario);
        reciboData.nome_cargo = checkAndParseString(reciboData.nome_cargo);
        reciboData.horas_trabalhadas = checkAndParse(reciboData.horas_trabalhadas, 10,);
        reciboData.horas_extras_um = checkAndParse(reciboData.horas_extras_um, 10);
        reciboData.horas_extras_dois = checkAndParse(reciboData.horas_extras_dois, 10);
        reciboData.horas_noturnas = checkAndParse(reciboData.horas_noturnas, 10);
        reciboData.repouso_remunerado = checkAndParse(reciboData.repouso_remunerado, 10);
        reciboData.correcao_positiva = checkAndParse(reciboData.correcao_positiva, 10);
        reciboData.correcao_negativa = checkAndParse(reciboData.correcao_negativa, 10);
        reciboData.data_inicio = formatDate(reciboData.data_inicio);
        reciboData.data_fim = formatDate(reciboData.data_fim);
        reciboData.data_pagamento = formatDate(reciboData.data_pagamento);
        reciboData.valor_diarias = checkAndParse(reciboData.valor_diarias, 10);

        

        // Verifique se todos os campos obrigatórios estão preenchidos
        const requiredFields = ['data_inicio','data_fim', 'data_pagamento','nome_cargo','name_funcionario','horas_trabalhadas', 'horas_extras_um', 'horas_extras_dois', 'horas_noturnas', 'valor_diarias', 'correcao_positiva', 'correcao_negativa'];


        //Valida os dados enviados -> Valor fucionario === string // Demais tem que ser float.
        for (const field of requiredFields) {
        const value = reciboData[field];
        // Verifica se o campo é nome_funcionario
        if (field === 'name_funcionario'|| field === 'nome_cargo' ) {  
        if (typeof value !== 'string' || value.trim() === '') {
            console.error(`Campo obrigatório "${field}" é inválido.`);
            return;
        }
        } 

        // Verifica se o campo é data_inicio ou data_fim
        else if (field === 'data_inicio' || field === 'data_fim' || field === 'data_pagamento' ) {
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

        }   
        console.log('Dados do funcionário antes de enviar:', JSON.stringify(reciboData, null, 2));

        
        // Envie os dados para o backend
        const response = await fetch('http://127.0.0.1:5000/api/criar_recibo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(reciboData),
        mode:'cors'

        });
        
        //const responseData = await response.json();  // Caso você precise processar a resposta como JSON
        //console.log('Dados retornados pelo backend:', responseData);

        if (response.ok) {

        const contentType = response.headers.get('Content-Type');
        if (contentType && contentType.includes('application/pdf')) {  
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
        document.getElementById('printDocumentButton').onclick =  function() { 
            const a = document.createElement('a');
            //const url = window.URL.createObjectURL(blob);
            a.href = url;
            a.download = `${reciboData.name_funcionario}_olerite.pdf`;
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
                console.error('Erro: A resposta não é um PDF. Tipo de conteúdo:', contentType);
            }
            } else {
            console.error('Erro ao gerar o olerite:', response.statusText);
            }
            
    });


        // Fechar mensagens 
        messageDiv.addEventListener('click', function() {
        messageDiv.style.display = 'none'; // Esconde a mensagem ao clicar na mensagem
        location.reload(); // Recarrega a página ao fechar a mensagem
        });
    });

};