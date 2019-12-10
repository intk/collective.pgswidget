/*
	PGS Widget
*/

jQuery(document).ready(function() {

	if (jQuery("body.portaltype-event").length > 0) {
		var endpoint = "/pgsreview";
		var request_url = window.location.protocol + "//" + window.location.host + window.location.pathname + endpoint;
		var $pgsreview_container = jQuery("#pgs-user-reviews");

		if ($pgsreview_container.length > 0) {
			// load reviews
			$pgsreview_container.load(request_url, function(){
				// do something
			});
		} else {
			// do not load reviews
		}
	}
});
