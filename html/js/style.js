var POStags = ['CC', 'CD', 'DT', 'EX', 'IN', 'PDT', 'POS', 'PRP', 'PRP$', 'RP', 'SYM', 'TO', 'UH', 'WDT', 'WP', 'WP$', 'WRB'];


/*
 * Clicking anywhere in the browser retrieves info from dic.js
 * if such info exists
*/
/*$(document).click(function(event) {
    	createTooltip(event);                
});

function createTooltip(event){
	var lemmavalue = $(event.target).attr('lemma');
	if (lemmavalue !== undefined) {
	lemmavalue = lemmavalue.toLowerCase();
	};
	if (hiddenInfo[lemmavalue] === undefined) {
		$('div.tooltip').css({'display':'none'});
	} else {
		var posvalue = $(event.target).attr('POS').substring(0, 1).toLowerCase();
		for (d in hiddenInfo[lemmavalue]) {
			if (hiddenInfo[lemmavalue][d][0].substring(0, 1) == posvalue) {
				$('div.tooltip').html(hiddenInfo[lemmavalue][d]);
				};
			};
    	positionTooltip(event);
	};        
};

function positionTooltip(event){
    var tPosX = event.pageX - 0;
    var tPosY = event.pageY - -40;
    $('div.tooltip').css({'position': 'absolute', 'top': tPosY, 'left': tPosX, 'border':'2px solid black', 'color': 'blue', 'background': 'yellow', 'width': '20%', 'display':'block'});
};
*/




//Clicking anywhere in the browser retrieves a WordNet infobox
$(document).click(function(event) {
    createTooltip(event);                
});

function createTooltip(event){
	var lemmavalue = $(event.target).attr('lemma');
	var posvalue = $(event.target).attr('pos');
	
	//Do not show infobox *if it is not a word or *if it is a function word
	if (lemmavalue !== undefined && POStags.indexOf(posvalue) === -1) {
		//console.log(posvalue);
		//var ifrm = document.createElement('iframe');
		var ifrm = document.getElementsByTagName('iframe')[0];
        ifrm.setAttribute('src', 'http://wordnetweb.princeton.edu/perl/webwn?s=' + lemmavalue + '&sub=Search+WordNet&o2=&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&h=');
        //document.body.appendChild(ifrm);
		positionTooltip(event);
	} else {
		document.getElementsByTagName('iframe')[0].style.display = 'none';
	};
};        

function positionTooltip(event){
    var tPosX = event.pageX - 0;
    var tPosY = event.pageY - -40;
    $('iframe').css({'position': 'absolute', 'top': tPosY, 'left': tPosX, 'border':'2px solid black', 'width': '700px', 'height': '500px', 'display': 'block'});
};



//Open closes menu on the right side
var action = 1;

console.log(action);

/* Set the width of the side navigation to 250px and the left margin of the page content to 250px */
function openNav() {
	document.getElementById("mySidenav").style.width = "250px";
	document.getElementById("main").style.marginRight = "250px";
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
	document.getElementById("mySidenav").style.width = "0";
	document.getElementById("main").style.marginRight = "0";
	action = 1;
}

function showMenu() {
	if (action == 1) {
		openNav();
		action = 2;
		console.log(action);
		} else {
		closeNav();
	};
}

$('#navButton').click(function() {
	showMenu();
});
