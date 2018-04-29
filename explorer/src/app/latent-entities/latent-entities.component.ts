import { Component, OnInit, Input, ElementRef, ViewChild } from '@angular/core';
import {ExplorerApiService} from '../services/explorer-api.service';
import { Subscription } from 'rxjs/Subscription';
import * as d3 from 'd3';

@Component({
  selector: 'app-latent-entities',
  templateUrl: './latent-entities.component.html',
  styleUrls: ['./latent-entities.component.scss']
})
export class LatentEntitiesComponent implements OnInit {


  private latentEntityRequestSubscription : Subscription;
  private closestEntityRequestSubscription : Subscription;
  
  public selectedLatentEntity : any;
  public closestEntities : any;
  private latentEntities : any;
  private tipDisabled : boolean = true;
  
 // Latent Entities
 public latentCount : number = 5;
 
 @ViewChild('chart') chart: ElementRef;
 
   constructor(private bookQuery : ExplorerApiService, private el: ElementRef) { }
 
   public buildDistributionFigure(latentEntities) {
      let topicIDs = latentEntities[0].map((e,idx) => idx);
      let latentEntityIDs = latentEntities.map((e,idx) => idx);
      let topicData = latentEntities.map((le, idx) => {
        let accum = []
        le.reduce((a, b, idx) => accum[idx] = a + b, 0);
        return {
          latentEntity : idx,
          strengths : latentEntities[idx],
          data : accum.map((y, idx) => {return {y1: y, y0: y - le[idx], topicID: idx}})
        }
      });

     var margin = {top: 0, right: 0, bottom: 0, left: 0},
         width = 15*latentEntityIDs.length - margin.left - margin.right,
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
 
     z.domain(latentEntityIDs);
     
     var x = d3.scaleBand().rangeRound([0, width]).padding(0.1),
         y = d3.scaleLinear().rangeRound([height, 0]);
     
     var g = svg.append("g")
         .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
 
         x.domain(latentEntityIDs);
         y.domain([0, 100]);
       
         g.append("g")
         .attr("class", "axis axis--x")
         .attr("transform", "translate(0," + height + ")")
         .call(d3.axisBottom(x));
   
        g.append("g")
         .attr("class", "axis axis--y")
         .call(d3.axisLeft(y));
       
         var book = svg.selectAll(".book")
             .data(topicData)
           .enter().append("g")
             .attr("class", "g")
             .attr("transform", function(d) { return "translate(" + x(d.latentEntity) + ",0)"; });
       
       var bars = book.selectAll("rect")
             .data(function(d) {
                topicIDs.forEach((id) => {
                  d.data[id]['latentEntity'] = d.latentEntity;
                  d.data[id]['strengths'] = d.strengths;
                });
               return d.data; 
             })
           .enter().append("rect")
             .attr("width", x.bandwidth())
             .attr("y", function(d) { return y(d.y1); })
             .attr("height", function(d) { return y(d.y0) - y(d.y1); })
             .attr("stroke", (d) => {
              if (d.latentEntity == this.selectedLatentEntity) {
                return 'white'
              }
              return 'none'
            })
             .style("fill", function(d) { return z(d.topicID); })
           .on("mousemove", (d) => {
              if(!this.tipDisabled){
                  div.style("left", d3.event.pageX+10+"px");
                  div.style("top", d3.event.pageY-25+"px");
                  div.style("display", "inline-block");
                  div.html('<strong> Latent Entity '+ d.latentEntity +'<\strong><br>Topic ' + d.topicID + ': ' + (d.y1-d.y0).toFixed(2) + '%')
              }
            })
            .on('mouseout', (d) => {
               div.style("display", "none")
            })
             .on('click', (d) => {
               this.tipDisabled = true;
                div.style("display", "none")              
               console.log('FETCHING TOP ENTITIES FOR LATENT ENTITY: ', d.latentEntity)
               console.log(d.strengths);
               this.requestClosestEntities(d.latentEntity, d.strengths);
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
          this.tipDisabled=false;
   }

  ngOnInit() {
  }

  public requestClosestEntities(latentID, strengths) {
    this.selectedLatentEntity = latentID;
    if(this.closestEntityRequestSubscription) {
      this.closestEntityRequestSubscription.unsubscribe();
    }
    this.closestEntityRequestSubscription = this.bookQuery.requestClosestEntities(strengths).subscribe((res) => {
      console.log(res);
      this.closestEntities = res.closest;
      this.buildDistributionFigure(this.latentEntities)      
    })
  }

  public requestLatentEntities() {
    if (this.latentEntityRequestSubscription) {
      this.latentEntityRequestSubscription.unsubscribe();
    }
    this.latentEntityRequestSubscription = this.bookQuery.requestLatentEntities(this.latentCount).subscribe((res : {latent_entities : Array<Array<number>>}) => {
      this.latentEntities = res.latent_entities;
      this.buildDistributionFigure(res.latent_entities);
    });
  }

}
