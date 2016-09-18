import jm.audio.io.*;
import jm.audio.synth.*;
import jm.music.data.Note;
import jm.audio.AudioObject;
import jm.audio.Instrument;

/**
 * A basic additive synthesis instrument implementation
 * which implements an envelope and allows specification
 * of the overtone frequency ratios and volume levels.
 * It implements frequency, envelope, volume, and panoramic control, in real time.
 * @author Andrew Brown, Andrew Sorensen, and Bill Manaris
 */
public final class AdditiveSynthesisInstrument extends Instrument
{
	//----------------------------------------------
	// Attributes
	//----------------------------------------------
	
	/** The number of channels */
	private int channels = 2;
	/** the sample rate passed to the instrument */
	private int sampleRate = 44100;
	/** The pitch in hertz of a fixed frequency oscillator */
	private float frequency = 440.0f;

	/** the relative overtoneRatios which make up this note */
	private double[] overtoneRatios;
	/** the overtoneVolumes to use for each frequency */
	private double[] overtoneVolumes;
	/** The points to use in the construction of Envelopes */
	private double[][] allEnvPoints;
	/** The break point values for the amplitude envelope (1D list of float pairs - time percent index in generated note (0.0 to 1.0) and amplitude (0.0 to 1.0) at corresponding time index */
	private double[] envelopePoints = {0.0, 0.0, 
	                                   0.05, 1.0, 
	                                   0.15, 0.4, 
	                                   0.9, 0.3, 
	                                   1.0, 0.0};

	/** The volume of the instrument (0.0 to 1.0) */
	private double volume = 1.0;	
	/** The panoramic of the instrument (0.0, left to 1.0, right) */
	private double panoramic = 0.5;

    /** Sound components */
    private Oscillator[] oscillatorBoxes;
	private Envelope[] envelopeBoxes;
	private	Volume[] overtoneVolumeBoxes;  // separate volumes for each overtone
	private Add adderBox;
	private	Volume volumeBox;              // global/total volume
	private	StereoPan panoramicBox;
    private SampleOut soutBox;


	//----------------------------------------------
	// Constructors
	//----------------------------------------------
	
	/**
	* Basic default constructor to set an initial sampling rat.
	* @param sampleRate
	*/
	public AdditiveSynthesisInstrument(int sampleRate){
		//Provide some defaults
		this.sampleRate = sampleRate;
		this.channels = 2;
		
		double[][] tempPoints = new double[5][];   // *** (BZM) Why only 5?
		for (int i=0; i<5; i++) {
			tempPoints[i] = this.envelopePoints;
		}
		this.allEnvPoints = tempPoints;
		
		double[] ratios =  {1.0f, 3.0f, 5.0f, 7.0f, 9.0f};
		this.overtoneRatios = ratios;
		double[] volumes = {1.0f, 0.5f, 0.35f, 0.25f, 0.15f};
		this.overtoneVolumes = volumes;
	}
	/**
	* Basic default constructor to set an initial 
	* sampling rate and buffersize in addition
	* to the neccessary frequency relationships 
	* and overtoneVolumes for each frequency to be added
	* the instrument
	* @param sampleRate 
	* @param overtoneRatios the relative freqencies to use
	* @param overtoneVolumes the overtoneVolumes to use for the overtoneRatios
	* @param EnvPointArray A two dimensional array of doubles as break point values between 0.0 and 1.0
	* @param frequency a positive float value specifying a fixed pitch
	*/
	public AdditiveSynthesisInstrument(int sampleRate, int channels, 
	                                   double[] overtoneRatios, double[] overtoneVolumes, 
	                                   double[][] envPointArray, float frequency)
    {
		this.sampleRate = sampleRate;
		this.channels = channels;
		this.overtoneRatios = overtoneRatios;
		this.overtoneVolumes = overtoneVolumes;
		this.allEnvPoints = envPointArray; 		
		this.frequency = frequency; 		
	}

	//----------------------------------------------
	// Methods 
	//----------------------------------------------
	/**
	 * Initialisation method is used to build the objects that
	 * this instrument will use
	 */
	public void createChain()
	{
		this.oscillatorBoxes = new Oscillator[ this.overtoneRatios.length ];
		this.envelopeBoxes = new Envelope[ this.overtoneRatios.length ];
		this.overtoneVolumeBoxes = new Volume[ this.overtoneRatios.length ];

        // create audio object chain
		for (int i = 0; i < overtoneRatios.length; i++)
		{
			this.oscillatorBoxes[i] = new Oscillator(this, Oscillator.SINE_WAVE, 
                                                     this.sampleRate, this.channels);
			this.envelopeBoxes[i]  = new Envelope(this.oscillatorBoxes[i], this.allEnvPoints[i]);
			//this.overtoneVolumeBoxes[i] = new Volume(this.envelopeBoxes[i], (float)this.overtoneVolumes[i]);
			this.overtoneVolumeBoxes[i] = new Volume(this.envelopeBoxes[i]);
			this.oscillatorBoxes[i].setFrqRatio( (float)overtoneRatios[i] );
		}

		this.setFrequency( this.frequency );   // set initial frequency
		this.setVolume( this.volume );         // set max volume (to avoid clipping)

		//And now the add object brings us back to one patch.
		this.adderBox = new Add( this.overtoneVolumeBoxes );

        // setup box to control final volume (since we are adding many indivdual oscillations,
        // each with its own volume)
		//this.volumeBox = new Volume( this.adderBox );        
		
        //this.panoramicBox = new StereoPan( this.volumeBox );
        this.panoramicBox = new StereoPan( this.adderBox );

        // decide if to generate live sound, or to write in an audio file
		if (output == RENDER) 
		   this.soutBox = new SampleOut( this.panoramicBox );        
	}

	/**
	* Set the frequency of the oscillator.
	* @param frequency - The frequency in hertz
	*/
	public void setFrequency(float frequency) 
	{
	    this.frequency = frequency;
		for (int i = 0; i < overtoneRatios.length; i++)
		{
            //this.oscillatorBoxes[i].setChoice(0);
			this.oscillatorBoxes[i].setFrq( this.frequency); 
			this.oscillatorBoxes[i].setFrqRatio(this.overtoneRatios[i] );
			//this.oscillatorBoxes[i].setFrqRatio( (float)this.overtoneRatios[i] );
		}
	}
        
	/**
	* Get the frequency of the oscillator.
	*/
	public float getFrequency() 
	{
	    return this.frequency;
	}
        
    /**
    * Set the sound envelope.
    * @param envelopePoints - The array of time percent, amplitude pairs of double values.
    */
    public void setEnvelopePoints(double[][] envelopePoints) 
    {
        this.allEnvPoints = envelopePoints;
    }
	
    /**
    * Get the sound envelope.
    */
    public double[][] getEnvelopePoints() 
    {
        return this.allEnvPoints;
    }
			
    /**
    * Set the sound volume.
    * @param volume - The new volume (0.0 to 1.0).
    */
    public void setVolume(double volume) 
    {
        this.volume = volume;
        /**
        * Since we have many oscillators each contributing their own volume,
        * we need to figure out a factor by which to multiply the global volume here,
        * so that we do not clip (i.e., exceed 1.0).  In particular when parameter
        * 'volume' is 1.0, we need to adjust the global volume so that the signal's
        * components' volumes add up to 1.0.
        */
        
        // calculate total component volume
        float totalVolume = 0;
		for (int i = 0; i < overtoneVolumes.length; i++)
        {
            System.out.println("overtoneVolume[" + i + "] = " + this.overtoneVolumes[i]);
            totalVolume += this.overtoneVolumes[i];  
        }
        // now, 'totalVolume' has the accumulated volume of all components
        System.out.println("totalVolume = " + totalVolume);
        
		for (int i = 0; i < overtoneVolumes.length; i++)
        {
            this.overtoneVolumeBoxes[i].setVolume(this.overtoneVolumes[i] / totalVolume);
        }
        // set global volume to a normalized value (e.g., if parameter 'volume' is 1.0,
        // global volume will be set to such a value, as to the accumulated volume of
        // all oscillators, passing through 'this.volumeBox' will equal 1.0 at the end.
        //this.volumeBox.setVolume(volume / totalVolume);
        //System.out.println("volume set to " + volume / totalVolume);
    }
		
    /**
    * Get the sound volume.
    */
    public double getVolume() 
    {
        return this.volume;
    }
	
	
    /**
    * Set the stereo panoramic.
    * @param panoramic - The new panoramic (0.0 to 1.0).
    */
    public void setPanoramic(double panoramic) 
    {
        this.panoramic = panoramic;
        this.panoramicBox.setPan( this.panoramic );
    }

    /**
    * Get the stereo panoramic.
    */
    public double getPanoramic() 
    {
        return this.panoramic;
    }
}
