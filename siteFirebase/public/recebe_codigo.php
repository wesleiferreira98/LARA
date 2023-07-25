<?php
    // Pasta onde o arquivo vai ser salvo
    $_UP['pasta'] = 'arquivos/';
    
    // Tamanho máximo do arquivo (em Bytes)
    $_UP['tamanho'] = 1024 * 1024 * 15; // 15Mb
    
    // Verifica se o conteúdo do editor foi recebido
    if (!isset($_POST['editor_content'])) {
        die("Nenhum conteúdo de editor recebido");
    }

    $conteudo = $_POST['editor_content'];

    // Verifica se o conteúdo parece ser Python
    if (!preg_match('/\b(import|for|if|print|while|def|class|else|elif|try|except|raise|finally|with|return|break|continue|del|pass|yield|lambda|nonlocal|global|assert)\b/', $conteudo)) {
        die("O conteúdo não parece ser código Python");
    }

    // Faz a verificação do tamanho do conteúdo
    if ($_UP['tamanho'] < strlen($conteudo)) {
        echo "O arquivo enviado é muito grande, envie arquivos de até 15Mb.";
    } else {
        // Cria um nome baseado no UNIX TIMESTAMP atual e com extensão .py
        $nome_final = time().'.py';

        // Tenta escrever o conteúdo para um novo arquivo
        if (file_put_contents($_UP['pasta'] . $nome_final, $conteudo) !== false) {
            // Upload efetuado com sucesso, exibe uma mensagem e um link para o arquivo
            echo "Upload efetuado com sucesso!";
            echo '<br /><a href="' . $_UP['pasta'] . $nome_final . '">Clique aqui para acessar o arquivo</a>';
        } else {
            // Não foi possível escrever o arquivo
            echo "Não foi possível enviar o arquivo, tente novamente";
        }
    }
?>
