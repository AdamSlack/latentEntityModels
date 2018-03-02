import { Component, OnInit, Input, ElementRef, ViewChild } from '@angular/core';
import {ExplorerApiService} from '../services/explorer-api.service';
import { Subscription } from 'rxjs/Subscription';
import * as d3 from 'd3';

@Component({
  selector: 'app-topic-models',
  templateUrl: './topic-models.component.html',
  styleUrls: ['./topic-models.component.scss']
})
export class TopicModelsComponent implements OnInit {

  public bookTitleSubscription : Subscription;
  public topicDisributionSubscriptions : Array<Subscription>;
  public topicDistributions : Array<{book: string, topics : Array<{topic_id: number, score: number}>}> = [];
  public sortKey : number = 0;
  

  @ViewChild('chart') chart: ElementRef;

  constructor(private api : ExplorerApiService, private el: ElementRef) { }

  public buildDistributionFigure() {
    console.log('Building D3 Chart.')
    
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

    let topicIDs = [0,1,2,3,4,5,6,7,8,9];
    let books = this.topicDistributions.map((t) => t.book);
    let topicData = this.topicDistributions.map((t, idx) =>  {
      let scores = t.topics.map((t) => t.score)
      let sum = scores.reduce((a,b) => a + b, 0);
      let pct = scores.map((s) => ((s/sum) * 100));
      let accum = []
      pct.reduce((a,b,i) => accum[i] = a + b,0);
      return {book: books[idx], data: accum.map((y, idx) => {return {y1: y, y0: y - pct[idx], topicID: idx}}) }
    });

    let data = topicData.sort((a,b) =>  (b.data[this.sortKey].y1 - b.data[this.sortKey].y0) - (a.data[this.sortKey].y1 -a.data[this.sortKey].y0));
    console.log('All Data:');
    console.log(this.topicDistributions); 
    
    console.log('Book Titles: ');
    console.log(books);

    console.log('Topic Scores: ');
    console.log(data);

    var margin = {top: 0, right: 0, bottom: 0, left: 0},
        width = 2999 - margin.left - margin.right,
        height = 360 - margin.top - margin.bottom;
        
    var svg = d3.select(this.chart.nativeElement)
    svg.selectAll('*').remove();
    svg.attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");

    var g = svg.append('g').attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
   
    
    var z = d3.scaleOrdinal(d3.schemeCategory10)
        .domain(topicIDs); 
    // z = d3.scaleOrdinal()
    // .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

    z.domain(d3.keys(data[0]).filter(function(key) { return key !== "book"; }));
    
    var x = d3.scaleBand().rangeRound([0, width]).padding(0.1),
        y = d3.scaleLinear().rangeRound([height, 0]);
    
    var g = svg.append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        x.domain(data.map(function(d) { return d.book; }));
        y.domain([0, 100]);
      
        g.append("g")
        .attr("class", "axis axis--x")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));
  
       g.append("g")
        .attr("class", "axis axis--y")
        .call(d3.axisLeft(y));
      
        var book = svg.selectAll(".book")
            .data(data)
          .enter().append("g")
            .attr("class", "g")
            .attr("transform", function(d) { return "translate(" + x(d.book) + ",0)"; });
      
      var bars = book.selectAll("rect")
            .data(function(d) {
              d.data.book_title = d.book; 
              return d.data; 
            })
          .enter().append("rect")
            .attr("width", x.bandwidth())
            .attr("y", function(d) { return y(d.y1); })
            .attr("height", function(d) { return y(d.y0) - y(d.y1); })
            .style("fill", function(d) { return z(d.topicID); })
            .on("mousemove", (d) => {
              div.style("left", d3.event.pageX+10+"px");
              div.style("top", d3.event.pageY-25+"px");
              div.style("display", "inline-block");
              console.log(d);
              div.html('<strong>' + d.book_title + '</strong>');
            })
            .on('mouseout', (d) => {
              div.style("display", "none")
            });

        var div = d3.select("body").append("div").attr("class", "toolTip");
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
  }

  ngOnInit() {
    this.bookTitleSubscription = this.api.requestBookTitles().subscribe((titleRes) => {
      this.topicDisributionSubscriptions = titleRes.books.map((book) => {
        return this.api.requestBookTopics(book).subscribe((bookRes) => {
          this.topicDistributions.push(bookRes)
          if(this.topicDistributions.length == titleRes.books.length){
            this.buildDistributionFigure();
          }
        });
      });
    });
  }

}
