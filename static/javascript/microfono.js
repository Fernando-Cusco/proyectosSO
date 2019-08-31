
        function speak(id) {
            var rec;
        if(!("webkitSpeechRecognition" in window)){
            alert("Tu naveganor no soporta");
        } else {
            if(id == 1){
            rec = new webkitSpeechRecognition();
            rec.lang = "en-US";
            rec.continuos = true;
            rec.interim = true;
            rec.addEventListener("result", iniciar);
            }
        }
        rec.start();
        }
        function iniciar(event){
            var t = 0;
            for(i = event.resultIndex; i < event.results.length; i++){
                var x = document.getElementById("textito");
                t = i;
                //alert(x.value+" "+event.results.length);
            }
            x.value = event.results[t][0].transcript;
        }


        function idButton() {
            speak(1);
        }
