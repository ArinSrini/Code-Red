// JavaScript for sender.html
$(document).ready(function() {
    $('#recordButton').click(function() {
        $.ajax({
            url: '/record_audio',
            type: 'POST',
            success: function(response) {
                alert('Audio recorded and encrypted successfully!');
            },
            error: function(error) {
                console.error('Error recording audio:', error);
            }
        });
    });
});

// JavaScript for receiver.html
$(document).ready(function() {
    $('#decryptForm').submit(function(event) {
        event.preventDefault();
        var privateKey = $('#privateKey').val();

        $.ajax({
            url: '/decrypt',
            type: 'POST',
            data: {
                private_key: privateKey
            },
            success: function(response) {
                alert('Audio decrypted and reconstructed successfully!');
            },
            error: function(error) {
                console.error('Error decrypting audio:', error);
            }
        });
    });
});
