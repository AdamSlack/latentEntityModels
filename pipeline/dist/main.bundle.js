webpackJsonp(["main"],{

/***/ "../../../../../src/$$_lazy_route_resource lazy recursive":
/***/ (function(module, exports) {

function webpackEmptyAsyncContext(req) {
	// Here Promise.resolve().then() is used instead of new Promise() to prevent
	// uncatched exception popping up in devtools
	return Promise.resolve().then(function() {
		throw new Error("Cannot find module '" + req + "'.");
	});
}
webpackEmptyAsyncContext.keys = function() { return []; };
webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
module.exports = webpackEmptyAsyncContext;
webpackEmptyAsyncContext.id = "../../../../../src/$$_lazy_route_resource lazy recursive";

/***/ }),

/***/ "../../../../../src/app/app.component.html":
/***/ (function(module, exports) {

module.exports = "<app-banner></app-banner>\n<div>\n  <app-book-explorer></app-book-explorer>\n</div>"

/***/ }),

/***/ "../../../../../src/app/app.component.scss":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/app.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return AppComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};

var AppComponent = (function () {
    function AppComponent() {
        this.title = 'app';
    }
    AppComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'app-root',
            template: __webpack_require__("../../../../../src/app/app.component.html"),
            styles: [__webpack_require__("../../../../../src/app/app.component.scss")]
        })
    ], AppComponent);
    return AppComponent;
}());



/***/ }),

/***/ "../../../../../src/app/app.module.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return AppModule; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_platform_browser__ = __webpack_require__("../../../platform-browser/esm5/platform-browser.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__angular_common_http__ = __webpack_require__("../../../common/esm5/http.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__angular_forms__ = __webpack_require__("../../../forms/esm5/forms.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_4__app_component__ = __webpack_require__("../../../../../src/app/app.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_5__book_explorer_book_explorer_component__ = __webpack_require__("../../../../../src/app/book-explorer/book-explorer.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_6__services_explorer_api_service__ = __webpack_require__("../../../../../src/app/services/explorer-api.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_7__banner_banner_component__ = __webpack_require__("../../../../../src/app/banner/banner.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_8__bannegstr_bannegstr_component__ = __webpack_require__("../../../../../src/app/bannegstr/bannegstr.component.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_9__topic_models_topic_models_component__ = __webpack_require__("../../../../../src/app/topic-models/topic-models.component.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};










var AppModule = (function () {
    function AppModule() {
    }
    AppModule = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_1__angular_core__["E" /* NgModule */])({
            declarations: [
                __WEBPACK_IMPORTED_MODULE_4__app_component__["a" /* AppComponent */],
                __WEBPACK_IMPORTED_MODULE_5__book_explorer_book_explorer_component__["a" /* BookExplorerComponent */],
                __WEBPACK_IMPORTED_MODULE_7__banner_banner_component__["a" /* BannerComponent */],
                __WEBPACK_IMPORTED_MODULE_8__bannegstr_bannegstr_component__["a" /* BannegstrComponent */],
                __WEBPACK_IMPORTED_MODULE_9__topic_models_topic_models_component__["a" /* TopicModelsComponent */]
            ],
            imports: [
                __WEBPACK_IMPORTED_MODULE_0__angular_platform_browser__["a" /* BrowserModule */],
                __WEBPACK_IMPORTED_MODULE_2__angular_common_http__["b" /* HttpClientModule */],
                __WEBPACK_IMPORTED_MODULE_3__angular_forms__["a" /* FormsModule */]
            ],
            providers: [__WEBPACK_IMPORTED_MODULE_6__services_explorer_api_service__["a" /* ExplorerApiService */]],
            bootstrap: [__WEBPACK_IMPORTED_MODULE_4__app_component__["a" /* AppComponent */]]
        })
    ], AppModule);
    return AppModule;
}());



/***/ }),

/***/ "../../../../../src/app/bannegstr/bannegstr.component.css":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/bannegstr/bannegstr.component.html":
/***/ (function(module, exports) {

module.exports = "<p>\n  bannegstr works!\n</p>\n"

/***/ }),

/***/ "../../../../../src/app/bannegstr/bannegstr.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return BannegstrComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var BannegstrComponent = (function () {
    function BannegstrComponent() {
    }
    BannegstrComponent.prototype.ngOnInit = function () {
    };
    BannegstrComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'app-bannegstr',
            template: __webpack_require__("../../../../../src/app/bannegstr/bannegstr.component.html"),
            styles: [__webpack_require__("../../../../../src/app/bannegstr/bannegstr.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], BannegstrComponent);
    return BannegstrComponent;
}());



/***/ }),

/***/ "../../../../../src/app/banner/banner.component.html":
/***/ (function(module, exports) {

module.exports = "<div class=\"banner\">\n  <div class=\"title\">\n    Latent Entity Models\n  </div>\n</div>"

/***/ }),

/***/ "../../../../../src/app/banner/banner.component.scss":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "div.banner {\n  width: 100%;\n  background: #227722;\n  padding: 20px;\n  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 2px 4px rgba(0, 0, 0, 0.24); }\n\ndiv.title {\n  color: #fff;\n  font-family: 'Roboto', sans-serif;\n  font-size: 20px; }\n", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/banner/banner.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return BannerComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var BannerComponent = (function () {
    function BannerComponent() {
    }
    BannerComponent.prototype.ngOnInit = function () {
    };
    BannerComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'app-banner',
            template: __webpack_require__("../../../../../src/app/banner/banner.component.html"),
            styles: [__webpack_require__("../../../../../src/app/banner/banner.component.scss")]
        }),
        __metadata("design:paramtypes", [])
    ], BannerComponent);
    return BannerComponent;
}());



/***/ }),

/***/ "../../../../../src/app/book-explorer/book-explorer.component.html":
/***/ (function(module, exports) {

module.exports = "<div class=\"container\">\n  <div class=\"title\">\n    📚 Books\n  </div>\n  <div class=\"entity-collection\">\n    <table class=\"entity-collection\">\n      <tr *ngFor=\"let title of bookTitles\" [ngClass]=\"(title==selectedBook)?'selected':''\">\n        <td (click)=\"requestEntities(title); requestTopics(title);\">\n          {{title}}\n        </td>\n      </tr>\n    </table>\n  </div>\n</div>\n\n<div class=\"container\">\n  <div class=\"title\">\n    🕮 Topics\n  </div>\n  <div class=\"entity-collection\">\n    <table class=\"entity-collection\">\n      <tr *ngFor=\"let topic of topics\" >\n        <td>\n          {{topic.id}}\n        </td>\n        <td>\n          {{topic.pct}}\n        </td>\n      </tr>\n    </table>\n  </div>\n</div>\n\n<div class=\"container\">\n  <div class=\"title\">\n    Distributions\n  </div>\n  <div class=\"entity-collection\">\n      <app-topic-models></app-topic-models>      \n  </div>\n</div>\n\n<div class=\"container\">\n  <div class=\"title\">\n    👤 Entities\n  </div>\n  <div class=\"entity-collection\">\n    <table class=\"entity-collection\">\n      <tr *ngFor=\"let entity of entities\" [ngClass]=\"(entity==selectedEntity)?'selected':''\">\n        <td (click)=\"requestEntityTerms(entity)\">\n          {{entity}}\n        </td>\n      </tr>\n    </table>\n  </div>\n</div>\n\n<div class=\"container\">\n  <div class=\"title\">\n    📃 {{selectedEntity}}\n  </div>\n  <div class=\"entity-collection\">\n    <table class=\"entity-collection\">\n      <tr *ngFor=\"let term of terms\">\n        <td>\n          {{term.term}}\n        </td>\n        <td>\n            {{term.strength}}\n        </td>\n      </tr>\n    </table>\n  </div>\n</div>\n\n<div class=\"container\">\n  <div class=\"title\">\n    📃 {{selectedEntity}} topic Distributions\n  </div>\n  <div class=\"entity-collection\">\n    <table class=\"entity-collection\">\n      <tr *ngFor=\"let topic of entityTopics\">\n        <td>\n          {{topic.topicID}}\n        </td>\n        <td>\n          {{topic.pct}}\n        </td>\n      </tr>\n    </table>\n  </div>`\n</div>\n\n\n"

/***/ }),

/***/ "../../../../../src/app/book-explorer/book-explorer.component.scss":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "div.entity-collection {\n  font-family: 'Roboto', sans-serif;\n  padding: 15px;\n  max-height: 400px;\n  min-height: 400px;\n  overflow-x: auto;\n  overflow-y: scroll; }\n  div.entity-collection::-webkit-scrollbar {\n    width: 6px;\n    background-color: #222; }\n  div.entity-collection::-webkit-scrollbar-thumb {\n    background-color: #666;\n    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3); }\n\ndiv.visualisation {\n  font-family: 'Roboto', sans-serif;\n  padding: 15px;\n  max-height: 400px;\n  min-height: 400px;\n  overflow-x: auto;\n  overflow-y: scroll; }\n  div.visualisation::-webkit-scrollbar {\n    width: 6px;\n    background-color: #222; }\n  div.visualisation::-webkit-scrollbar-thumb {\n    background-color: #666;\n    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3); }\n\n.selected {\n  transition: background-color 0.2s ease;\n  background: #ddd !important;\n  color: #222 !important; }\n\ntable.entity-collection {\n  font-family: 'Roboto', sans-serif;\n  width: 100%;\n  border-collapse: collapse;\n  border-top: solid 1px #333;\n  transition: background-color 0.2s ease; }\n  table.entity-collection tr {\n    background: #222;\n    border-bottom: solid 1px #333; }\n    table.entity-collection tr:hover {\n      background: #333;\n      transition: background-color 0.2s ease; }\n    table.entity-collection tr td {\n      padding-top: 5px;\n      padding-bottom: 5px; }\n\n.title {\n  font-size: 20px;\n  padding: 10px;\n  margin: auto;\n  font-family: 'Roboto', sans-serif;\n  color: #ddd; }\n\n.container {\n  color: #ddd;\n  background: #222;\n  padding: 5px;\n  margin: 5px;\n  width: 20%;\n  float: left;\n  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 2px 4px rgba(0, 0, 0, 0.24);\n  min-width: 400px; }\n", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/book-explorer/book-explorer.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return BookExplorerComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__services_explorer_api_service__ = __webpack_require__("../../../../../src/app/services/explorer-api.service.ts");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};


var BookExplorerComponent = (function () {
    function BookExplorerComponent(bookQuery) {
        this.bookQuery = bookQuery;
        this.selectedEntity = 'Select an Entity';
        this.selectedBook = 'select a book';
        this.topicIDs = [];
        this.topicTerms = [];
        this.entityTopics = [];
        this.topicTermSubscriptions = [];
    }
    BookExplorerComponent.prototype.requestEntityTerms = function (entity) {
        var _this = this;
        if (this.entityTermSubscription) {
            this.entityTermSubscription.unsubscribe();
        }
        this.entityTermSubscription = this.bookQuery.requestEntityTerms(this.selectedBook, entity).subscribe(function (res) {
            _this.selectedEntity = entity;
            _this.terms = res.terms;
            _this.mapEntityTermTopics();
        });
    };
    BookExplorerComponent.prototype.requestEntities = function (bookTitle) {
        var _this = this;
        this.selectedBook = bookTitle;
        this.entitySubscription = this.bookQuery.requestEntities(bookTitle).subscribe(function (res) {
            _this.entities = res.entities;
        });
    };
    BookExplorerComponent.prototype.mapEntityTermTopics = function () {
        console.log(this.terms);
        console.log(this.topicTerms);
        var entityTerms = this.terms.map(function (t) { return t.term.toLowerCase(); });
        var presentTerms = this.topicTerms.map(function (topic) {
            return {
                topicID: topic.topic_id,
                terms: topic.terms.filter(function (term) { return entityTerms.indexOf(term.term.toLowerCase()) > -1; })
            };
        });
        console.log('Present Terms');
        console.log(presentTerms);
        var topicScores = presentTerms.map(function (t) {
            return { topicID: t.topicID, score: t.terms.reduce(function (a, b) { return a + b.strength; }, 0) };
        });
        console.log('Topic Scores');
        console.log(topicScores);
        var sum = topicScores.reduce(function (a, b) { return a + b.score; }, 0);
        this.entityTopics = topicScores.map(function (t) {
            return { topicID: t.topicID, pct: ((t.score / sum) * 100).toFixed(2) };
        });
        console.log('Entity Topics');
        console.log(this.entityTopics);
    };
    BookExplorerComponent.prototype.requestTopics = function (bookTitle) {
        var _this = this;
        if (this.bookTopicSubscription) {
            this.bookTopicSubscription.unsubscribe();
        }
        this.bookTopicSubscription = this.bookQuery.requestBookTopics(bookTitle).subscribe(function (res) {
            var api_topics = res.topics;
            var sum = api_topics.reduce(function (a, b) { return a + b.score; }, 0);
            _this.topics = api_topics.map(function (t) {
                return { id: 'Topic ' + t.topic_id.toString(), pct: (t.score / sum * 100).toFixed(2) };
            }).sort(function (a, b) { return b.pct - a.pct; });
        });
    };
    BookExplorerComponent.prototype.requestTopicIDs = function () {
        var _this = this;
        if (this.topicIDSubscription) {
            this.topicIDSubscription.unsubscribe();
        }
        this.topicIDSubscription = this.bookQuery.requestTopicIDs().subscribe(function (res) {
            _this.topicIDs = res.topic_ids;
            _this.topicTermSubscriptions.length = _this.topicIDs.length;
            _this.topicTerms.length = _this.requestTopicIDs.length;
            _this.topicIDs.forEach(function (id) { return _this.requestTopicTerm(id); });
        });
    };
    BookExplorerComponent.prototype.requestTopicTerm = function (topicID) {
        var _this = this;
        if (this.topicTermSubscriptions[topicID]) {
            this.topicTermSubscriptions[topicID].unsubscribe();
        }
        this.topicTermSubscriptions[topicID] = this.bookQuery.requestTopicTerms(topicID).subscribe(function (res) {
            _this.topicTerms[topicID] = res;
        });
        console.log(this.topicTerms);
    };
    BookExplorerComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.bookTitleSubscription = this.bookQuery.requestBookTitles().subscribe(function (res) {
            _this.bookTitles = res.books;
        });
        this.requestTopicIDs();
    };
    BookExplorerComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'app-book-explorer',
            template: __webpack_require__("../../../../../src/app/book-explorer/book-explorer.component.html"),
            styles: [__webpack_require__("../../../../../src/app/book-explorer/book-explorer.component.scss")]
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1__services_explorer_api_service__["a" /* ExplorerApiService */]])
    ], BookExplorerComponent);
    return BookExplorerComponent;
}());



/***/ }),

/***/ "../../../../../src/app/services/explorer-api.service.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return ExplorerApiService; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_common_http__ = __webpack_require__("../../../common/esm5/http.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_rxjs_add_operator_toPromise__ = __webpack_require__("../../../../rxjs/_esm5/add/operator/toPromise.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_rxjs_add_operator_toPromise___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_2_rxjs_add_operator_toPromise__);
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var ExplorerApiService = (function () {
    function ExplorerApiService(http) {
        this.http = http;
        this.ROOT = 'http://grapesoda.hopto.org/api/';
    }
    ExplorerApiService.prototype.requestEntities = function (book_title) {
        // example... 'http://localhost:8080/stockbroker?stockID=AMG&granularity=TIME_SERIES_DAILY'
        var url = this.ROOT + 'books/' + book_title;
        console.log(url);
        return this.http.get(url);
    };
    ExplorerApiService.prototype.requestEntityTerms = function (book_title, entity) {
        // example... 'http://localhost:8080/stockbroker?stockID=AMG&granularity=TIME_SERIES_DAILY'
        var url = this.ROOT + 'books/' + book_title + '/entities/' + entity;
        console.log(url);
        return this.http.get(url);
    };
    ExplorerApiService.prototype.requestBookTopics = function (book_title) {
        var url = this.ROOT + 'books/' + book_title + '/topics';
        console.log(url);
        return this.http.get(url);
    };
    ExplorerApiService.prototype.requestBookTitles = function () {
        var url = this.ROOT + 'books';
        console.log(url);
        return this.http.get(url);
    };
    ExplorerApiService.prototype.requestTopicIDs = function () {
        var url = this.ROOT + 'topics';
        console.log('url');
        return this.http.get(url);
    };
    ExplorerApiService.prototype.requestTopicTerms = function (topicID) {
        var url = this.ROOT + 'topics/' + topicID.toString();
        console.log('url');
        return this.http.get(url);
    };
    ExplorerApiService = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["w" /* Injectable */])(),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1__angular_common_http__["a" /* HttpClient */]])
    ], ExplorerApiService);
    return ExplorerApiService;
}());



/***/ }),

/***/ "../../../../../src/app/topic-models/topic-models.component.html":
/***/ (function(module, exports) {

module.exports = "\n<input type=\"number\" [(ngModel)]=sortKey (change)=buildDistributionFigure() step=\"1\" max=\"9\">\n<div>\n  <svg #chart></svg>\n</div>\n"

/***/ }),

/***/ "../../../../../src/app/topic-models/topic-models.component.scss":
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__("../../../../css-loader/lib/css-base.js")(false);
// imports


// module
exports.push([module.i, "", ""]);

// exports


/*** EXPORTS FROM exports-loader ***/
module.exports = module.exports.toString();

/***/ }),

/***/ "../../../../../src/app/topic-models/topic-models.component.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return TopicModelsComponent; });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__services_explorer_api_service__ = __webpack_require__("../../../../../src/app/services/explorer-api.service.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2_d3__ = __webpack_require__("../../../../d3/index.js");
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var TopicModelsComponent = (function () {
    function TopicModelsComponent(api, el) {
        this.api = api;
        this.el = el;
        this.topicDistributions = [];
        this.sortKey = 0;
    }
    TopicModelsComponent.prototype.buildDistributionFigure = function () {
        var _this = this;
        console.log('Building D3 Chart.');
        // let data = this.topicDistributions.map((d) => {
        //   return {
        //     book: d.book,
        //     topic_0: d.topics[0],
        //     topic_1: d.topics[1],
        //     topic_2: d.topics[2],
        //     topic_3: d.topics[3],
        //     topic_4: d.topics[4],
        //     topic_5: d.topics[5],
        //     topic_6: d.topics[6],
        //     topic_7: d.topics[7],
        //     topic_8: d.topics[8],
        //     topic_9: d.topics[9],
        //   }
        // });
        var topicIDs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
        var books = this.topicDistributions.map(function (t) { return t.book; });
        var topicData = this.topicDistributions.map(function (t, idx) {
            var scores = t.topics.map(function (t) { return t.score; });
            var sum = scores.reduce(function (a, b) { return a + b; }, 0);
            var pct = scores.map(function (s) { return ((s / sum) * 100); });
            var accum = [];
            pct.reduce(function (a, b, i) { return accum[i] = a + b; }, 0);
            return { book: books[idx], data: accum.map(function (y, idx) { return { y1: y, y0: y - pct[idx], topicID: idx }; }) };
        });
        var data = topicData.sort(function (a, b) { return (b.data[_this.sortKey].y1 - b.data[_this.sortKey].y0) - (a.data[_this.sortKey].y1 - a.data[_this.sortKey].y0); });
        console.log('All Data:');
        console.log(this.topicDistributions);
        console.log('Book Titles: ');
        console.log(books);
        console.log('Topic Scores: ');
        console.log(data);
        var margin = { top: 0, right: 0, bottom: 0, left: 0 }, width = 3000 - margin.left - margin.right, height = 380 - margin.top - margin.bottom;
        var svg = __WEBPACK_IMPORTED_MODULE_2_d3__["i" /* select */](this.chart.nativeElement);
        svg.selectAll('*').remove();
        svg.attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
        var g = svg.append('g').attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
        var z = __WEBPACK_IMPORTED_MODULE_2_d3__["g" /* scaleOrdinal */](__WEBPACK_IMPORTED_MODULE_2_d3__["h" /* schemeCategory10 */])
            .domain(topicIDs);
        // z = d3.scaleOrdinal()
        // .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);
        z.domain(__WEBPACK_IMPORTED_MODULE_2_d3__["d" /* keys */](data[0]).filter(function (key) { return key !== "book"; }));
        var x = __WEBPACK_IMPORTED_MODULE_2_d3__["e" /* scaleBand */]().rangeRound([0, width]).padding(0.1), y = __WEBPACK_IMPORTED_MODULE_2_d3__["f" /* scaleLinear */]().rangeRound([height, 0]);
        var g = svg.append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
        x.domain(data.map(function (d) { return d.book; }));
        y.domain([0, 100]);
        g.append("g")
            .attr("class", "axis axis--x")
            .attr("transform", "translate(0," + height + ")")
            .call(__WEBPACK_IMPORTED_MODULE_2_d3__["a" /* axisBottom */](x));
        g.append("g")
            .attr("class", "axis axis--y")
            .call(__WEBPACK_IMPORTED_MODULE_2_d3__["b" /* axisLeft */](y));
        var book = svg.selectAll(".book")
            .data(data)
            .enter().append("g")
            .attr("class", "g")
            .attr("transform", function (d) { return "translate(" + x(d.book) + ",0)"; });
        var bars = book.selectAll("rect")
            .data(function (d) {
            d.data.book_title = d.book;
            return d.data;
        })
            .enter().append("rect")
            .attr("width", x.bandwidth())
            .attr("y", function (d) { return y(d.y1); })
            .attr("height", function (d) { return y(d.y0) - y(d.y1); })
            .style("fill", function (d) { return z(d.topicID); })
            .on("mousemove", function (d) {
            div.style("left", __WEBPACK_IMPORTED_MODULE_2_d3__["c" /* event */].pageX + 10 + "px");
            div.style("top", __WEBPACK_IMPORTED_MODULE_2_d3__["c" /* event */].pageY - 25 + "px");
            div.style("display", "inline-block");
            console.log(d);
            div.html('<strong>' + d.book_title + '</strong>');
        })
            .on('mouseout', function (d) {
            div.style("display", "none");
        });
        var div = __WEBPACK_IMPORTED_MODULE_2_d3__["i" /* select */]("body").append("div").attr("class", "toolTip");
        div.style('position', 'absolute')
            .style('display', 'none')
            .style('width', 'auto')
            .style('height', 'auto')
            .style('background', 'rgba(34,34,34,0.8)')
            .style('border', '0 none')
            .style('border', 'radius 8px 8px 8px 8px')
            .style('box-shadow', '0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24)')
            .style('color', '#fff')
            .style('font-size', '0.75em')
            .style('padding', '5px')
            .style('text-align', 'left');
    };
    TopicModelsComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.bookTitleSubscription = this.api.requestBookTitles().subscribe(function (titleRes) {
            _this.topicDisributionSubscriptions = titleRes.books.map(function (book) {
                return _this.api.requestBookTopics(book).subscribe(function (bookRes) {
                    _this.topicDistributions.push(bookRes);
                    if (_this.topicDistributions.length == titleRes.books.length) {
                        _this.buildDistributionFigure();
                    }
                });
            });
        });
    };
    __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["_3" /* ViewChild */])('chart'),
        __metadata("design:type", __WEBPACK_IMPORTED_MODULE_0__angular_core__["r" /* ElementRef */])
    ], TopicModelsComponent.prototype, "chart", void 0);
    TopicModelsComponent = __decorate([
        Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["m" /* Component */])({
            selector: 'app-topic-models',
            template: __webpack_require__("../../../../../src/app/topic-models/topic-models.component.html"),
            styles: [__webpack_require__("../../../../../src/app/topic-models/topic-models.component.scss")]
        }),
        __metadata("design:paramtypes", [__WEBPACK_IMPORTED_MODULE_1__services_explorer_api_service__["a" /* ExplorerApiService */], __WEBPACK_IMPORTED_MODULE_0__angular_core__["r" /* ElementRef */]])
    ], TopicModelsComponent);
    return TopicModelsComponent;
}());



/***/ }),

/***/ "../../../../../src/environments/environment.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "a", function() { return environment; });
// The file contents for the current environment will overwrite these during build.
// The build system defaults to the dev environment which uses `environment.ts`, but if you do
// `ng build --env=prod` then `environment.prod.ts` will be used instead.
// The list of which env maps to which file can be found in `.angular-cli.json`.
var environment = {
    production: false
};


/***/ }),

/***/ "../../../../../src/main.ts":
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__angular_core__ = __webpack_require__("../../../core/esm5/core.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__angular_platform_browser_dynamic__ = __webpack_require__("../../../platform-browser-dynamic/esm5/platform-browser-dynamic.js");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_2__app_app_module__ = __webpack_require__("../../../../../src/app/app.module.ts");
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_3__environments_environment__ = __webpack_require__("../../../../../src/environments/environment.ts");




if (__WEBPACK_IMPORTED_MODULE_3__environments_environment__["a" /* environment */].production) {
    Object(__WEBPACK_IMPORTED_MODULE_0__angular_core__["_8" /* enableProdMode */])();
}
Object(__WEBPACK_IMPORTED_MODULE_1__angular_platform_browser_dynamic__["a" /* platformBrowserDynamic */])().bootstrapModule(__WEBPACK_IMPORTED_MODULE_2__app_app_module__["a" /* AppModule */])
    .catch(function (err) { return console.log(err); });


/***/ }),

/***/ 0:
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__("../../../../../src/main.ts");


/***/ })

},[0]);
//# sourceMappingURL=main.bundle.js.map