/*
 * Copyright (c) 2019.
 * Ahmad Syafiq Kamil
 */

(function( window, undefined ) {

var Globalize;

if ( typeof require !== "undefined" &&
	typeof exports !== "undefined" &&
	typeof module !== "undefined" ) {
	// Assume CommonJS
	Globalize = require( "globalize" );
} else {
	// Global variable
	Globalize = window.Globalize;
}

Globalize.addCultureInfo( "ta", "default", {
	name: "ta",
	englishName: "Tamil",
	nativeName: "தமிழ்",
	language: "ta",
	numberFormat: {
		groupSizes: [3,2],
		percent: {
			groupSizes: [3,2]
		},
		currency: {
			pattern: ["$ -n","$ n"],
			groupSizes: [3,2],
			symbol: "ரூ"
		}
	},
	calendars: {
		standard: {
			"/": "-",
			firstDay: 1,
			days: {
				names: ["ஞாயிற்றுக்கிழமை","திங்கள்கிழமை","செவ்வாய்கிழமை","புதன்கிழமை","வியாழக்கிழமை","வெள்ளிக்கிழமை","சனிக்கிழமை"],
				namesAbbr: ["ஞாயிறு","திங்கள்","செவ்வாய்","புதன்","வியாழன்","வெள்ளி","சனி"],
				namesShort: ["ஞா","தி","செ","பு","வி","வெ","ச"]
			},
			months: {
				names: ["ஜனவரி","பிப்ரவரி","மார்ச்","ஏப்ரல்","மே","ஜூன்","ஜூலை","ஆகஸ்ட்","செப்டம்பர்","அக்டோபர்","நவம்பர்","டிசம்பர்",""],
				namesAbbr: ["ஜனவரி","பிப்ரவரி","மார்ச்","ஏப்ரல்","மே","ஜூன்","ஜூலை","ஆகஸ்ட்","செப்டம்பர்","அக்டோபர்","நவம்பர்","டிசம்பர்",""]
			},
			AM: ["காலை","காலை","காலை"],
			PM: ["மாலை","மாலை","மாலை"],
			patterns: {
				d: "dd-MM-yyyy",
				D: "dd MMMM yyyy",
				t: "HH:mm",
				T: "HH:mm:ss",
				f: "dd MMMM yyyy HH:mm",
				F: "dd MMMM yyyy HH:mm:ss",
				M: "dd MMMM",
				Y: "MMMM yyyy"
			}
		}
	}
});

}( this ));
