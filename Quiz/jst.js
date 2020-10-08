var content=[{question:"When did India get Independence?",
              options:["1946","1947","1948","1949"],
              correct:2},
              {question:"Who is the Prime minister of India?",
              options:["Narendra Modi","Manmohan Singh","Rahul Gandi","Amith Sha"],
              correct:1},
              {question:"Who is the Chief minister of Kerala?",
              options:["Pinarayi Vijayan","Oommen Chandi","VS Achuthanathan","Ramesh Chennithala"],
              correct:1},
              {question:"The World Largest desert is?",
              options:["Thar","Kalahari","Sahara","Sonoran"],
              correct:3},
              {question:"Which of the following is the capital of Arunachal Pradesh?",
              options:["Itanagar","Dispur","Imphal","Panaji"],
              correct:1},
              {question:"Which state has the largest area?",
              options:["Maharashtra","Madhya Pradesh","Uttar Pradesh","Rajasthan"],
              correct:4}
            ];
var total=6;
var correct=0;
var current=0;
function addContent(){
  if(current<total){
    document.querySelector(".question").innerText=current+1+'.'+content[current].question;
    document.querySelector('#o1+span').textContent=content[current].options[0];
    document.querySelector('#o2+span').textContent=content[current].options[1];
    document.querySelector('#o3+span').textContent=content[current].options[2];
    document.querySelector('#o4+span').textContent=content[current].options[3];
  }
  else{

    document.querySelector(".question").innerHTML="Marks: "+correct;
    document.querySelector(".options").style.display = "none";
    document.querySelector(".next").style.display = "none";

  }
}
function next(){

    let optn=document.getElementsByName('options');

    let selected;
    for(i=0;i<optn.length;i++){
      if(optn[i].checked){
        selected=optn[i].value;
        optn[i].checked=false;
        break;
      }
    }
    if(selected==content[current].correct){
        correct++;
    }
    current++;
    addContent();
}
